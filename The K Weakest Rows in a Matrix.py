class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        mat_idx = list(enumerate(mat))
        sorted_rows = sorted(mat_idx, key=lambda x: (sum(x[1]), x[0]))
        weakest_rows = [x[0] for x in sorted_rows]
        return weakest_rows[:k]

s = Solution()

print(s.kWeakestRows([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))


 
