# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
#
# A row i is weaker than a row j if one of the following is true:
#
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        mat_idx = list(enumerate(mat))
        print(mat_idx)
        sorted_rows = sorted(mat_idx, key=lambda x: (sum(x[1]), x[0]))
        weakest_rows = [x[0] for x in sorted_rows]
        return weakest_rows[:k]

s = Solution()

print(s.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))


 
