class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # print(len(matrix))
        len_mat, len_list = len(matrix), len(matrix[0])

        r, l = 0, len_list - 1

        while r < len_mat and l >= 0:
            if matrix[r][l] > target:
                l -= 1
            elif matrix[r][l] < target:
                r += 1

            elif matrix[r][l] == target:
                return True

        return False



        