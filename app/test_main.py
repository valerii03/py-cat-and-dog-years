from app.main import get_human_age


def test_zero_ages() -> None:
    """Test cat_age=0 and dog_age=0"""
    assert get_human_age(0, 0) == [0, 0]


def test_below_first_threshold() -> None:
    """Test ages below first threshold (15 years)"""
    assert get_human_age(14, 14) == [0, 0]


def test_at_first_threshold() -> None:
    """Test ages exactly at first threshold (15 years)"""
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    """Test ages between 15 and 24 years"""
    assert get_human_age(23, 23) == [1, 1]


def test_at_second_threshold() -> None:
    """Test ages exactly at second threshold (24 years)"""
    assert get_human_age(24, 24) == [2, 2]


def test_between_second_and_next_increment() -> None:
    """Test ages just above second threshold but not enough for next increment"""
    assert get_human_age(27, 27) == [2, 2]


def test_next_increment_cat_only() -> None:
    """Test ages where cat gets next increment before dog"""
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    """Test very large ages"""
    assert get_human_age(100, 100) == [21, 17]