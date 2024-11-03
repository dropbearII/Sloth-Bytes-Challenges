import numbers_to_english as n


def test_zero():
    assert n.num_to_eng(0) == "zero"


def test_greater_than_999():
    assert n.num_to_eng(1000) == "Number has to be in range [0,999]"


def test_18():
    assert n.num_to_eng(18) == 'eighteen'


def test_30():
    assert n.num_to_eng(30) == 'thirty'


def test_126():
    assert n.num_to_eng(126) == 'one hundred twenty six'


def test_909():
    assert n.num_to_eng(909) == 'nine hundred nine'
