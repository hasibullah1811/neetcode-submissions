class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Binary Search

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
    

        while top <= bottom:
            middleRow = (top + bottom) // 2
            if matrix[middleRow][-1] < target:
                top = middleRow + 1
            elif matrix[middleRow][0] > target:
                bottom = middleRow - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        middleRow = (top + bottom) // 2
        l, r = 0, cols - 1

        while (l <= r):
            m = (l + r) // 2
            if target > matrix[middleRow][m]:
                l = m + 1
            elif target < matrix[middleRow][m]:
                r = m - 1
            else:
                return True
        return False
