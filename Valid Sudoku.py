class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subarrays = []
        for i in (0, 3, 6):
            for j in (3, 6, 9):
                subarray = board[i][(j - 3):j] + board[i + 1][(j - 3):j] + board[i + 2][(j - 3):j]
                subarrays.append(subarray)
        for i in range(10):
            for subarray in subarrays:
                if subarray.count(i) not in (0, 1):
                    return False
            for row in board:
                if row.count(i) not in (0, 1):
                    return False
            for column in zip(*board):
                if column.count(i) not in (0, 1):
                    return False
        return True

