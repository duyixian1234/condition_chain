import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from condition_chain.__version__ import __version__

def test_version():
    assert __version__