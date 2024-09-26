import convenience_store


def test_enough_change():
    assert convenience_store.change_enough([2, 100, 0, 0], 14.11) is False
    assert convenience_store.change_enough([0, 0, 20, 5], 0.75) is True
    assert convenience_store.change_enough([30, 40, 20, 5], 12.55) is True
    assert convenience_store.change_enough([10, 0, 0, 50], 3.85) is False
    assert convenience_store.change_enough([1, 0, 5, 219], 19.99) is False

