import valid_java_comments as v


def test_multiple_single_comments():
    assert v.java_comments_correct("//////") is True


def test_single_comment():
    assert v.java_comments_correct("//") is True


def test_multiline_comment():
    assert v.java_comments_correct("/**/") is True


def test_multiline_comment_not_opened():
    assert v.java_comments_correct("*/") is False


def test_multiline_comment_not_closed():
    assert v.java_comments_correct("/*") is False


def test_mixed():
    assert v.java_comments_correct("/**//**////**/") is True


def test_incorrect_single_comments():
    assert v.java_comments_correct("/////") is False
