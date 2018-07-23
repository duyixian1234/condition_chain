import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_differ():
    assert Condition(1).differ(2).result() is True

def test_not_differ():
    assert Condition(1).differ(1).result() is False

def test_differ_success():
    condition = Condition(1)
    condition.differ(2)
    assert ('differ', 2) in condition.success

def test_differ_failure():
    condition = Condition(1)
    condition.differ(1)
    assert ('differ', 1) in condition.failures