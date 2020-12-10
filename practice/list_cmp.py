import time

one_to_ten = [x for x in range(1, 11)]
# print(one_to_ten)

nine = [y for y in range(2, 10)][-1]
# print(nine)

first_ten_squares = [num ** 2 for num in range(1, 11)]
# print(first_ten_squares)

first_ten_even_nums = [eve_num for eve_num in range(2, 21, 2)]
# print(first_ten_even_nums)

first_five_even_nums = [n for n in first_ten_even_nums if n <= 10]
# print(first_five_even_nums)

# Nested for loops using list comprehensions
st_time = time.time()
list_of_tups2 = [(num, letter) for num in range(1, 5) for letter in 'abcd']
# print(list_of_tups2)
# print(f'Diff2: {int(time.time() - st_time)}')

# Dict comprehensions
# zip(list1,list2) -> creates a list of tuples based on values in list1 and list2
members = ["Luffy", "Zoro", "Sanji"]
roles = ["Captain", "Swordsman", "Chef"]
mem_roles = {member: role for (member, role) in zip(members, roles)}
print(mem_roles)
