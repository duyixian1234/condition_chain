import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_be():
    assert Condition(1).be(1).result() is True

def test_not_be():
    assert Condition(1).be(2).result() is False

def test_be_success():
    condition = Condition(1)
    condition.be(1)
    assert ('be', 1) in condition.success

def test_be_failure():
    condition = Condition(1)
    condition.be(2)
    assert ('be', 2) in condition.failures