import keyboard_shortcut as ks


def test_ctrlC_crtlV():
    assert ks.keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon") == "the egg and the egg and the spoon"


def test_ctrlV_ctrlC():
    assert ks.keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") == "WARNING WARNING"


def test_ctrlC_ctrlV_twice():
    assert ks.keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") == "The The Town The The Town"
