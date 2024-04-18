from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    # Obter todas as categorias
    categories = [news["category"] for news in find_news()]

    # Contar ocorrências de cada categoria
    category_counts = Counter(categories)

    # Ordenar categorias por contagem: mais frequente para menos frequente
    def sort_key(item):
        return -item[1], item[0]

    sorted_categories = sorted(category_counts.items(), key=sort_key)
    # Extrair os nomes das cinco primeiras categorias
    result = [category for category, _ in sorted_categories[:5]]

    return result
