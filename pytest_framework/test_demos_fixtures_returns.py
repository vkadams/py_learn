import pytest

@pytest.fixture
def setup(): # by default scope='function'
    print('setup browser...')
    return "Chrome" # returns something

def test_mytest(setup):
    print('test_mytest')
    print('Browser is:',setup) # we can use the return into test function

def test_mytest2():
    print('test_mytest2')

def test_mytest3():
    print('test_mytest3')