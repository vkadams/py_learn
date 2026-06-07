from random import shuffle
example = [1,2,3,4,5,6,7]
shuffle(example)
#print(example) # shuffles everytime

# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
#
# result = shuffle_list(example)
# #print(result)
#
# # a game
# def player_guess():
#     guess = ''
#     while guess not in ['0', '1', '2']:
#         guess = input('Enter your guess (0 or 1 or 2): ')
#
#     return int(guess)
#
# my_index = player_guess()
# print('Player guessed=',my_index)
#
# # lets write another function to check the guess-- functions interacting with each other
# def check_guess(mylist, guess):
#     if mylist[my_index] == 'O':
#         print('Correct')
#     else:
#         print('Wrong guess')
#         print(mylist)
#
#
# # the logic
# # initial list
# mylist = ['', 'O', '']
# # shuffle list
# mixedup_list = shuffle_list(mylist)
# # user guess
# guess = player_guess()
# # check guess
# check_guess(mixedup_list, guess)

def shuf_list(lst):
    shuffle(lst)
    return lst

def pl_gu():
    gu = ''
    while gu not in ['0', '1', '2']:
        gu = input('Enter 0 or 1 or 2: ')

    return int(gu)

the_index = pl_gu()
print(the_index)

def chk_gu(lst, gu):
    if lst[gu] == 'O':
        print('WOW')
        print(lst)
    else:
        print('NAH')
        print(lst)

lst = ['', 'O', '']
lst = shuf_list(lst)
gu = pl_gu()
chk_gu(lst, gu)