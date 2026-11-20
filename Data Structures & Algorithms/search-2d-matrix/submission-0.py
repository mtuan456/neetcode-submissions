class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1

        while left <= right:
            mid = (right + left)//2
            e = mid // n
            r = mid % n

            if matrix[e][r] > target:
                right = mid - 1

            elif matrix[e][r] < target:
                left = mid + 1
            else:
                return True
        return False

        