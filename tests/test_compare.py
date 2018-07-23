import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain import Condition

def test_equal_num():
    assert Condition(1).equal(1).result() is True

def test_unequal_num():
    assert Condition(1).equal(2).result() is False

def test_equal_object():
    assert Condition([1, 2]).equal([1, 2]).result() is True

def test_unequal_object():
    assert Condition([]).equal('').result() is False

def test_equal_success():
    condition = Condition(1)
    condition.equal(1)
    assert ('equal', 1) in condition.success

def test_equal_failure():
    condition = Condition(1)
    condition.equal(0)
    assert ('equal', 0) in condition.failures

def test_gt():
    assert Condition(1).gt(0).result() is True

def test_not_gt():
    assert Condition(1).gt(2).result() is False

def test_gt_success():
    condition = Condition(1)
    condition.gt(0)
    assert ('gt', 0) in condition.success

def test_gt_failure():
    condition = Condition(1)
    condition.gt(2)
    assert ('gt', 2) in condition.failures

def test_lt():
    assert Condition(1).lt(2).result() is True

def test_not_lt():
    assert Condition(1).lt(0).result() is False

def test_lt_success():
    condition = Condition(1)
    condition.lt(2)
    assert ('lt', 2) in condition.success

def test_lt_failure():
    condition = Condition(1)
    condition.lt(0)
    assert ('lt', 0) in condition.failures