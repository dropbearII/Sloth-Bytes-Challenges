import simon_says_parser as s


def test_ignore_false_line():
    assert s.simon_says([
        "Simon says add 4",
        "Simon says add 6",
        "Then add 5"
    ]) == 10


def test_correct_parsing():
    assert s.simon_says([
        "Susan says add 10",
        "Simon says add 3",
        "Simon says multiply by 8"
    ]) == 24


def test_typo_name():
    assert s.simon_says([
        "Firstly, add 4",
        "Simeon says subtract 100"  # Look at the name closely :)
    ]) == 0
