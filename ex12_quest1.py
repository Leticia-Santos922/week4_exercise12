# obj: Understand the syntax for tuples, lists and dictionaries

# TODO: what is wrong with the below code

# list can be iterable
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# python interpret 'oke' string as an iterable (means you can iterate over the characters)
# cheese += 'Oke'  # each character of oke as an individual item to the list

# a) how should oke be added to the end of the list?
# compound logic operations (research)
# += is a shorthand assignment operator which is used to concatenate (add) to sequences (list)
cheese += ['Oke']  # needed the [] brackets as added entire list to the end of the cheese to add Oke
print(cheese)

# can be used to add more than one value
# cheese += ['Oke', 'Leicester']
# print(cheese)


# TODO: adding an item at the beginning of a list (things to look after the homework)
# TODO: adding an item in the middle of the list (things to look at after the homework)


# b) how would you add two new cheese with a single command?

print(f"added to cheese list: {cheese + ['Oke', 'Leceister']}")

# extend method Equivalent to my_list.extend([4, 5])
