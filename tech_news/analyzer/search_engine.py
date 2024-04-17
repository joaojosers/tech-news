from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"title": {"$regex": f"{title}", "$options": "i"}}
        )
    ]


# Requisito 8

def search_by_date(date):
    try:
        return [
            (news["title"], news["url"])
            for news in search_news(
                {
                    "timestamp": datetime.strptime(date, "%Y-%m-%d")
                    .date()
                    .__format__("%d/%m/%Y")
                }
            )
        ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_category(category):
    return [
        (news["title"], news["url"])
        for news in search_news(
            {"category": {"$regex": f"^{category}$", "$options": "i"}}
        )
    ]
