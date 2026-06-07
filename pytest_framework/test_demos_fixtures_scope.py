import pytest
'''
scope of fixtures:
scope="function" fixture will be called before every test function executes
scope="module" fixture will be called only once before test function executes
scope="class" fixture will be called only once before the class
scope="session" fixture will be called only once for session
typical hierarchy-->
module--> class --> methods
module--> functions
'''
@pytest.fixture
def setup(scope="module"):
    print('setup browser...') # mostly used to invoke browsers

def test_mytest(setup):
    print('test_mytest')
def test_mytest2(setup):
    print('test_mytest2')
def test_mytest3(setup):
    print('test_mytest3')