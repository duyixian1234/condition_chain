import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_contain():
    assert Condition('abc').contain('a').result() is True

def test_not_contain():
    assert Condition('abc').contain('d').result() is False

def test_contain_success():
    condition = Condition('abc')
    condition.contain('a')
    assert ('contain', 'a') in condition.success

def test_contain_failure():
    condition = Condition('abc')
    condition.contain('d')
    assert ('contain', 'd') in condition.failures