import pytest

# fixture- reusable function and is not a test function
@pytest.fixture
def setup():
    print('setup')
@pytest.fixture
def teardown():
    print('teardown')

# we need to pass the fixture function as parameter for test functions
def test_mytest(setup,teardown):
    print('test_mytest')
def test_mytest2(setup,teardown):
    print('test_mytest2')
def test_mytest3(setup, teardown):
    print('test_mytest3')
