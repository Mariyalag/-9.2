first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(str) for str in first_strings if len(str) >= 5]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {str: len(str) for str in first_strings + second_strings if len(str) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)












# def by_3(x):
#      return x * 3


# def is_odd(x):
#     return x % 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(by_3, filter(is_odd, my_numbers))
#
# print(list(result))

# пример 2
# аналог map

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = [x * 3 for x in my_numbers]
#
# print(result)

# пример 3 - списковая сборка с if
# аналог filter

# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_numbers if x % 2]
#
# print(result)

# пример 4 - уссловия перед циклом (для того чтобы не отфильтровывать данные а поменять операцию над ними)
# my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
# result = [x if type(x) == str else x * 5 for x in my_numbers]
# print(result)

# пример 5 - можно делать вложенные циклы
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = [x * y for x in my_numbers for y in they_numbers]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result)

# пример 6 - можно создавать на лету множество и словари
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = {x for x in my_numbers}
# print(result)
#
# they_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = {x: x ** 2 for x in my_numbers}
# print(result)