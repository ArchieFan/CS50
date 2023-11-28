from seasons import convert_to_words

def test_convert_to_words():
    assert convert_to_words(18492) == "Twenty-six million, six hundred twenty-eight thousand, four hundred eighty minutes"
    assert convert_to_words(4925) == "Seven million, ninety-two thousand minutes"
