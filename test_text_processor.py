# import module
# from file import class

import pytest
from text_processor import TextProcessor


def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text("hello world")
    assert result == "HELLO WORLD"
    assert result != "hello world"

# 2. Assert not equal - nem egyenlő
def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    pass


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text("hello")
    assert "olleh" in result


def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    pass


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words("This is a test")
    assert isinstance(result, int)
    assert not isinstance(result, str)
    assert isinstance(result, int) and result == 4


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result = processor.count_words("One")
    result_two = processor.count_words("One two")
    result_three = processor.count_words("One two three")

    assert result < result_two
    assert result_two <= result_three
    assert result_three > result_two


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words("")
    assert result == 0


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    result_true = processor.is_palindrome("Anna")
    result_false = processor.is_palindrome("Hello")
    assert result_true is True
    assert result_false is False
    assert processor.is_palindrome("") is False
    assert processor.is_palindrome("Indul a görög aludni") is True

def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    projector = TextProcessor()
    result = projector.remove_spaces(" a b c ")
    assert len(result) == 3
    