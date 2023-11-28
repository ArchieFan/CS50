from twttr import shorten

def test_assert():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

def test_capitalized_vowel():
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("WhAt's yOUr nAmE?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"