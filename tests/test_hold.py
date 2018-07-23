import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_hold():
    assert Condition([1, 2, 3]).hold(3).result() is True

def test_not_hold():
    assert Condition([1, 2, 3]).hold(1).result() is False

def test_hold_success():
    condition = Condition([1, 2, 3])
    condition.hold(3)
    assert ('hold', 3) in condition.success

def test_hold_failure():
    condition = Condition([1, 2, 3])
    condition.hold(1)
    assert ('hold', 1) in condition.failures