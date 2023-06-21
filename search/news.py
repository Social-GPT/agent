import time
from itertools import islice
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import re
from llm import LLM, GenerationItemType, GenerationMode
from langchain.schema import HumanMessage
from logger import Logger

DUCKDUCKGO_MAX_ATTEMPTS = 3


def search_news_about(topic: str, num_results: int = 4) -> str:
    if not topic:
        return []
    search_results = []
    attempts = 0

    while attempts < DUCKDUCKGO_MAX_ATTEMPTS:
        results = DDGS().news(topic)
        search_results = list(islice(results, num_results))

        if search_results:
            break

        time.sleep(1)
        attempts += 1

    # Assuming each result is a dictionary with a 'url' key
    urls = [result['url'] for result in search_results]
    Logger.log('Searched in DuckDuckGo',
               f'Found {len(urls)} search results for query: {topic}')

    page_contents = read_urls(urls)

    # Combine the search results with their corresponding page contents
    for result, content in zip(search_results, page_contents):
        result['content'] = content or ""

    return search_results


def read_urls(urls: list):
    contents = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.text

            # Replace sequences of newline characters with a single newline
            text = re.sub('\n+', '\n', text)

            # Replace sequences of space characters with a single space
            text = re.sub(' +', ' ', text)

            Logger.log(
                'Read Url', f'The following url has been scrapped: {url}')

            summary = LLM.generate(
                [HumanMessage(content=f'Summarize in 150-200 words:\n\n{text[:1500]}')], GenerationItemType.NEWS_SUMMARY, GenerationMode.MEDIUM).content.strip()

            Logger.log(
                'Summarize Url', f'The following url has been summarized: {url}\n\n{summary}')

            contents.append(summary)

        except Exception as e:
            print(f"Failed to fetch content from {url}. Error: {e}")
    return contents
