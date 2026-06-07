import pytest

@pytest.fixture
def setup():
    print('setup environment')
    yield
    print('teardown environment')