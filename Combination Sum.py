# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
# of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.

from itertools import combinations_with_replacement

# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         result = []
#         for i in range(1, max(len(candidates), target) + 1):
#             for seq in combinations_with_replacement(candidates, i):
#                 if sum(seq) == target:
#                     result.append(seq)
#         return result
candidates = [7,5,8,12,3,10,9,4,11,6]
target = 21

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
     result = []
     for i in range(1, max(len(candidates), target) + 1):
         for seq in combinations_with_replacement(candidates, i):
             if sum(list(seq)) == target:
                 result.append(list(seq))
     return result

print(combinationSum(candidates, target))

