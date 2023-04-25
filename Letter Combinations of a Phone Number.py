# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
# could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keyboard = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        digits = digits.replace('1', '')
        digits_list = [keyboard[int(digit)] for digit in digits]
        combs = product(*digits_list)
        answer = [''.join(comb) for comb in combs]
        return answer












