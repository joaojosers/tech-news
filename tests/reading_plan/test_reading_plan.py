import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService
from tests.assets.news import NEWS


def news_mock():
    return NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch("tech_news.analyzer.reading_plan.find_news", news_mock)

    result = ReadingPlanService.group_news_for_available_time(2)

    assert len(result["readable"]) == 6
    assert len(result["unreadable"]) == 7

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)
