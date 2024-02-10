import random

# help(random)
# initialise an empty list
# TODO: 1 make a list 1 - 50 without inputting each integer
# write a program that generate and display 6 unique random lottery numbers between 1 - 50
# # created variable and assigned it to an empty list
lottery_list = []

# range generates numbers in specified range (6)
# for loop iterates over a range from 1 to 50
# range function - EXPLAIN
# for loop to iterate sequence of 6 empty values or containers
for num in range(6):
    # append function is to add to empty list value 1 item in the lottery list
    # randrange function from module creates a sequence which starts at 1 - 50 and picks random numbers
    lottery_list.append(random.randrange(1, 51))

# print function passes the
print(lottery_list)


# TODO: Go through this and check if can do alternative, also with tuples

# ALTERNATIVE
# one line of code
# created a variable assigned to combined functions list and range
# combined list function and range to directly convert the sequence of numbers by generated by range into a list
# lottery_list = list(range(1, 51))
#
# print(f"lottery numbers: {lottery_list.append(random.randrange(1, 51))}")

# for num in lottery_list:
# display 6 unique random lottery numbers between 1 and 50

# use python help() function to find out which function to use from the python standard library called random
#
# print(lottery_list)
#     lottery_list = random.randrange(1, 51)
#     print(f"lottery numbers: {lottery_list} * 6")
#     # for each iteration of this loop num take on the next value
#     lottery_list.append(num)

#  print(lottery_list)

# ALTERNATIVE (Tuples as they are immutable)
# lottery_tuple = tuple(range(1, 51))
# print(lottery_tuple)


# which python data structure best suited to store the numbers


