"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # First pass to find all rows and columns that need to be zeroed
        for row in range(rows):
            for column in range(cols):
                if matrix[row][column] == 0:
                    zero_rows.add(row)
                    zero_cols.add(column)


        # Second pass to set rows and columns to zero
        for row in zero_rows:
            for column in zero_cols:
                matrix[row][column] = 0
                
        for column in zero_cols:
            for row in zero_rows:   
                matrix[row][column] = 0
                

        return matrix

sol = Solution()
# Example 1: Output: [[1,0,1],[0,0,0],[1,0,1]]
matrix = [[1,1,1],[1,0,1],[1,1,1]]

print(sol.setZeroes(matrix=matrix))

# Example 2: Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(sol.setZeroes(matrix=matrix))