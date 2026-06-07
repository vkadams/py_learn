import pytest


def test_loginbyemail():
    print('This is login by email test')
    assert 1 == 1

@pytest.mark.skip(reason="skip test")
def test_loginbyfacebook():
    print('This is login by facebook test')
    assert 1 == 1


def test_loginbyphone():
    print('This is login by phone test')
    assert 1 == 1


def test_signupbyemail():
    print('This is signup by email test')
    assert 1 == 1

@pytest.mark.skip(reason="skip test")
def test_signupbyfacebook():
    print('This is signup by facebook test')
    assert 1 == 1

@pytest.mark.skip
def test_signupbyphone():
    print('This is signup by phone test')
    assert 1 == 1

# ctrl+alt+L to format codea