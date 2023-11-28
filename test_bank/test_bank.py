from bank import value

def test_greeted_by_zero():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hello") == 0
    assert value("hello, newman") == 0




def test_greeted_by_20():
    assert value("How you doing?") == 20
    assert value("HOW YOU DOING?") == 20
    assert value("how you doing?") == 20
    assert value("how you doing?") == 20

def test_greeted_by_100():
    assert value("What's happening?") == 100
    assert value("what's happening?") == 100
