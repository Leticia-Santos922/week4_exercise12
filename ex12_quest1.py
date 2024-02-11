# obj: Understand the syntax for tuples, lists and dictionaries

# TODO: what is wrong with the below code
# lists:
# ordered collections of objects (also known as sequences)
# objects containing a sequential collection of other objects called elements
# lists are mutable where they extend or shrink - new items can be added on or removed
# list can be iterable
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# python interpret 'oke' string as an iterable (means you can iterate over the characters)
# cheese += 'Oke'  # each character of oke is concatenated as an individual item to the list

# A) how should oke be added to the end of the list?
# compound logic operations (research)
# += is a shorthand assignment operator which is used to append (add) an element to sequences (list)
cheese += ['Oke']  # needed the [] brackets to be an element and added to the end of the cheese list to add Oke
print(cheese)

# b) how would you add two new cheese with a single command?

# Used + arithmatic operator concatenates the existing list cheese with the new list with two new cheese elements
# f-string formats the output message and uses {} and interpolates the expression cheese to concatenate to new list
# the print function stringifies the concatenated lists and message
print(f"added two new cheeses to the list: {cheese + ['Oke', 'Leceister']}")

# extend method Equivalent to my_list.extend([4, 5])
