import pytest

'''
1. ordering tests by position --
@pytest.mark.order(3), @pytest.mark.order(2), so on..
'''


# @pytest.mark.order(3)
# def test_logout():
#     print('This is logout test')
#
#
# @pytest.mark.order(1)
# def test_login():
#     print('This is login test')
#
#
# @pytest.mark.order(2)
# def test_add_item():
#     print('This is add item test')


# 2. using before, after

# @pytest.mark.order(after="test_add_item")
# def test_checkout():
#     print('This is checkout test')
#
#
# @pytest.mark.order(before="test_checkout")
# def test_add_item():
#     print('This is add item test')
#
#
# @pytest.mark.order(1)
# def test_login():
#     print('This is login test')
#
#
# # 3. using marker string [user defined string]
@pytest.mark.order("first")
def test_login():
    print('This is login test')

@pytest.mark.order()
def test_add_item():
    print('This is add item test')

@pytest.mark.order("last")
def test_checkout():
    print('This is checkout test')