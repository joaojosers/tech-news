import re
import parsel
import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


# Requisito 2
def scrape_updates(html_content):

    selector = parsel.Selector(html_content)
    news_links = selector.css('.entry-title > a::attr(href)').getall()

    return news_links


# Requisito 3
def scrape_next_page_link(html_content):

    selector = parsel.Selector(html_content)
    next_page_link = selector.css('.next.page-numbers::attr(href)').get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    # Criando um objeto Selector com o conteúdo HTML
    selector = Selector(html_content)

    # Obtendo o URL da notícia
    url = selector.css('link[rel="canonical"]::attr(href)').get()

# Obtendo o título da notícia
    title = selector.css(".entry-title::text").get().strip()
# title = selector.css('.single-article-header h1::text').get().strip()

    # Obtendo o timestamp da notícia
    timestamp = selector.css(".meta-date::text").get()

    # Obtendo o nome do autor da notícia
    writer = selector.css(".url.fn.n::text").get()

    # Obtendo o tempo estimado de leitura da notícia
    reading_time = selector.css('.reading-time::text').re_first(r'\d+')
    reading_time_string = (
        selector.css(".meta-reading-time::text").get().strip()
    )
    reading_time = int(re.sub("[^0-9]", "", reading_time_string))

    # Obtendo o resumo da notícia
    summary = (
        selector.xpath("//p").xpath("string()").get().strip()
    )

    # Obtendo a categoria da notícia
    category = selector.css(".meta-category .label::text").get()

    # Criando um dicionário com as informações da notícia
    news_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }

    return news_data


# Requisito 5
def get_tech_news(amount: int):
    BASE_URL = "https://blog.betrybe.com/"
    html_content = fetch(BASE_URL)
    news_urls = scrape_updates(html_content)
    news = list()
    for ind in range(amount):
        try:
            news.append(scrape_news(fetch(news_urls[ind])))
        except IndexError:
            html_content = fetch(scrape_next_page_link(html_content))
            news_urls.extend(scrape_updates(html_content))
            news.append(scrape_news(fetch(news_urls[ind])))

    create_news(news)
    return news
