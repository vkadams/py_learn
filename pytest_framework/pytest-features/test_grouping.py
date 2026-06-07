'''
Grouping strategy:
test_loginbyemail --> sanity, regression
test_loginbyfacebook --> sanity
test_loginbyphone --> regression
test_signupbyemail --> sanity, regression
test_signupbyfacebook --> regression
test_signupbyphone --> sanity
test_paymentindollar --> sanity, regression
test_paymentinrupees --> regression
'''

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print('This is to test login by email')
    assert 1 == 1

@pytest.mark.sanity
def test_loginbyfacebook():
    print('This is to test login by facebook')
    assert 1 == 1

@pytest.mark.regression
def test_loginbyphone():
    print('This is to test login by phone')
    assert 1 == 1

@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print('This is to test signup by email')
    assert 1 == 1

@pytest.mark.regression
def test_signupbyfacebook():
    print('This is to test signup by facebook')
    assert 1 == 1

@pytest.mark.sanity
def test_signupbyphone():
    print('This is to test signup by phone')
    assert 1 == 1

@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollars():
    print('This is to test payment in dollars')
    assert 1 == 1

@pytest.mark.regression
def test_paymentinrupees():
    print('This is to test payment in rupees')
    assert 1 == 1


'''
1- only sanity tests
py -m pytest test_grouping.py -s -v -m "sanity"

2- only regression tests
py -m pytest test_grouping.py -s -v -m "regression"

3- both sanity & regression tests
py -m pytest test_grouping.py -s -v -m "sanity and regression"

4- run only sanity tests which are not marked for regression
py -m pytest test_grouping.py -s -v -m "sanity" -m "not regression"

4- run only regression tests which are not marked for sanity
py -m pytest test_grouping.py -s -v -m "regression" -m "not sanity"
'''