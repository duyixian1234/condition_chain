import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_instance_of():
    assert Condition(1).instance_of(int).result() is True

def test_not_instance_of():
    assert Condition(1).instance_of(str).result() is False

def test_instance_of_success():
    condition = Condition(1)
    condition.instance_of(int)
    assert ('instance_of', int.__name__) in condition.success

def test_instance_of_failure():
    condition = Condition(1)
    condition.instance_of(str)
    assert ('instance_of', str.__name__) in condition.failures