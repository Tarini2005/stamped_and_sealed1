import pytest
from leetspeak.leetspeak import leetspeak

def test_basic_words():
    assert leetspeak("hello") == "#3110"
    assert leetspeak("leet") == "1337"

def test_mixed_case():
    assert leetspeak("PyThOn") == "|D`/7#0|\\|"

def test_special_characters():
    assert leetspeak("code!") == "<0|)|!"

def test_empty_string():
    assert leetspeak("") == ""

def test_numbers_unchanged():
    assert leetspeak("1234") == "1234"

if __name__ == "__main__":
    pytest.main()
