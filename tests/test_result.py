from condition_chain import Condition


def test_result_of_true():
    assert Condition(1).be(1).result() is True


def test_result_of_of_false():
    assert Condition(1).be(0).result() is False
