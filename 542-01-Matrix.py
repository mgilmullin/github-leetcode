"""
https://leetcode.com/problems/01-matrix/

542. 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Methodology BFS
        Start from each 0, find the distance between this 0 and each no-zero element. 
        Update the distance if the distance is shorter than the current.
        We traversal all elements of the list twice so time complexity is O(2mn) ~ O(n^2),
        where m is size of matrix and n is size of the columns.
        """
        q = collections.deque()
        row = len(mat)
        col = len(mat[0])
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        for x in range(row):
            for y in range(col):
                if mat[x][y] == 0:
                    q.append((x, y))

                else:
                    mat[x][y] = float("inf")

        while q:
            x, y = q.popleft()
            
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy

                if 0 <= newX < row and 0 <= newY < col and mat[newX][newY] > mat[x][y] + 1:
                    q.append((newX, newY))
                    mat[newX][newY] = mat[x][y] + 1

        return mat