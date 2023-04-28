# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
import collections


# def totalFruit(fruits: list[int]) -> int:
#     max_fruits = 0
#     for window_size in range(len(fruits) + 1):
#         if window_size > max_fruits + 1:
#             break
#         for idx, tree in enumerate(fruits):
#             window = fruits[idx:idx + window_size]
#             if len(set(window)) <= 2:
#                 if len(window) > max_fruits:
#                     max_fruits = len(window)
#                 elif len(window) == max_fruits:
#                     break
#             else:
#                 continue
#     return max_fruits
#
#
# print(totalFruit(fruits))
# fruits = [1, 1, 1, 1, 3, 4, 1, 2, 1]


# def totalFruit(fruits: list[int]) -> int:
#     if len(set(fruits)) <= 2:
#         return len(fruits)
#     max_fruits = 0
#     for idx, tree in enumerate(fruits):
#         if max_fruits > len(fruits[idx:]):
#             break
#         window_size = max_fruits + 1
#         window = fruits[idx:idx + window_size]
#         while len(set(window)) <= 2:
#             if len(window) > max_fruits:
#                 max_fruits = len(window)
#             window_size += 1
#             window = fruits[idx:idx + window_size]
#             if len(window) < window_size:
#                 break
#     return max_fruits


def totalFruit(fruits: list[int]) -> int:
    if len(set(fruits)) <= 2:
        return len(fruits)
    max_fruits = 0
    window_start = 0
    window_end = 1
    while True:

        window = fruits[window_start:window_end]
        if len(set(window)) <= 2:
            if len(window) > max_fruits:
                max_fruits = len(window)
            window_end += 1
            if window_end > len(fruits):
                break
        else:
            window_start += 1
            window_end += 1
        if max_fruits >= len(fruits[window_start:]):
            break
    return max_fruits





# Slow algorythm:

import re

# class Solution:
#     def totalFruit(self, fruits: list[int]) -> int:
#         if len(set(fruits)) > 1:
#             fruit_pairs = set([(x, y) for x in fruits for y in fruits if x != y])
#         else:
#             return len(fruits)
#         most_fruits = 0
#         for pair in fruit_pairs:
#             mapped_fruits = ['F' if fruit in pair else 'x' for fruit in fruits]
#             str_fruits = ''.join(mapped_fruits)
#             str_fruits = re.sub("x+", "x", str_fruits)
#             fruit_sequences = str_fruits.split('x')
#             result = len(max(fruit_sequences, key=len))
#             if result > most_fruits:
#                 most_fruits = result
#         return most_fruits


# import random
# fruits = [random.randint(0, 5) for i in range(6)]
# print(fruits)
# fruit_pairs = [[x, y] for x in fruits for y in fruits if x != y]
# fruit_pairs = set([tuple(sorted(pair)) for pair in fruit_pairs])

# most_fruits = 0
# for pair in fruit_pairs:
#     mapped_fruits = ['F' if fruit in pair else 'x' for fruit in fruits]
#     str_fruits = ''.join(mapped_fruits)
#     str_fruits = re.sub("x+", "x", str_fruits)
#     print(mapped_fruits)
#     fruit_sequences = str_fruits.split('x')
#     print(fruit_sequences)
#     result = len(max(fruit_sequences, key=len))
#     if result > most_fruits:
#         most_fruits = result
# # return most_fruits



