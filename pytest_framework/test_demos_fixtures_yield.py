import pytest
@pytest.fixture
def setup():
    print('setup browser...')
    yield
    print('teardown browser...')

'''
Execution:
setup browser will execute
then test_mytest function will execute
it sees yield- this will close browser
again- setup brower will execute
then test_mytest2 function will execute
and so on...
'''

def test_mytest(setup):
    print('This is test one')

def test_mytest2(setup):
    print('This is test two')

def test_mytest3(setup):
    print('This is test three')