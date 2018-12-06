from condition_chain import Condition


def test_expect():
    assert Condition('abc').expect(len, 3).result() is True


def test_not_expect():
    assert Condition('abc').expect(len, 2).result() is False


def test_expect_success():
    condition = Condition('abc')
    condition.expect(len, 3)
    assert ('expect', (len.__name__, 3)) in condition.success


def test_expect_failure():
    condition = Condition('abc')
    condition.expect(len, 2)
    assert ('expect', (len.__name__, 2)) in condition.failures
