from condition_chain import Condition


class Person():
    name = 'default'


def test_have():
    assert Condition(Person()).have('name').result() is True


def test_not_have():
    assert Condition(Person()).have('age').result() is False


def test_have_success():
    condition = Condition(Person())
    condition.have('name')
    assert ('have', 'name') in condition.success


def test_have_failure():
    condition = Condition(Person())
    condition.have('age')
    assert ('have', 'age') in condition.failures
