from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    try:
        assert convert("3/0") == 4
    except ZeroDivisionError:
        print("Y cannot be 0")
    try:
        assert convert("A/B") == 4
    except ValueError:
        print("X and Y must be integers")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"