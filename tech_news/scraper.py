import parsel
import requests
import time

# Requisito 1


def fetch(url: str) -> str:
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    finally:
        time.sleep(1)


def scrape_updates(html_content):

    selector = parsel.Selector(html_content)
    news_links = selector.css('.entry-title > a::attr(href)').getall()

    return news_links


def scrape_next_page_link(html_content):

    selector = parsel.Selector(html_content)
    next_page_link = selector.css('.next.page-numbers::attr(href)').get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
