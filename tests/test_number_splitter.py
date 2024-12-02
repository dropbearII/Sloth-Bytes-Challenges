import number_splitter as n


def test_positive_number():
    assert n.num_split(39) == [30, 9]


def test_negative_number():
    assert n.num_split(-434) == [-400, -30, -4]


def test_hundred():
    assert n.num_split(100) == [100, 0, 0]
