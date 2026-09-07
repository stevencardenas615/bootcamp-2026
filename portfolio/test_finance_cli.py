from datetime import datetime
from pathlib import Path
from finance_cli import AllowedCategory, app, search_builder

def test_search_builder_no_filters():
    where_prompts, parameters = search_builder()
    assert where_prompts == []
    assert parameters == []

def test_search_builder_all_filters():
    start = datetime(2026, 1, 1)
    end = datetime(2026, 1, 31)
    choice = AllowedCategory.RENT

    where_prompts, parameters = search_builder(choice=choice, start=start, end=end)
    assert where_prompts == ["category = ?", "date >= ?", "date <= ?"]
    assert parameters == ["rent", "2026-01-01", "2026-01-31"]

def test_search_builder_only_category():
    where_prompts, parameters = search_builder(choice=AllowedCategory.FOOD_DINING)
    assert where_prompts == ["category = ?"]
    assert parameters == ["food_dining"]

def test_search_builder_date_range_only():
    start = datetime(2026, 1, 1)
    end = datetime(2026, 2, 28)
    where_prompts, parameters = search_builder(start=start, end=end)
    assert where_prompts == ["date >= ?", "date <= ?"]
    assert parameters == ["2026-01-01", "2026-02-28"]

def test_search_builder_category_and_start_date():
    start = datetime(2026, 3, 15)
    where_prompts, parameters = search_builder(choice=AllowedCategory.TRANSPORTATION, start=start)
    assert where_prompts == ["category = ?", "date >= ?"]
    assert parameters == ["transportation", "2026-03-15"]

def test_search_builder_category_and_end_date():
    end = datetime(2026, 1, 15)
    where_prompts, parameters = search_builder(choice=AllowedCategory.TRANSPORTATION, end=end)
    assert where_prompts == ["category = ?", "date <= ?"]
    assert parameters == ["transportation", "2026-01-15"]

