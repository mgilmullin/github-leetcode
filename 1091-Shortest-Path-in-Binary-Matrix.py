"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
 

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 
Methodology: Breadth First Search (BFS)
Append the start path coordinate to queue. 
Use BFS traversal the 2D list from path coordinate pop out from queue. 
Each time expand the current path coordinate for 8 directions. 
The first path to reach bottom right will return the steps.


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

Complexity:
We iterate over all elements of 2D list once so total time complexity is O(n*n) where n is the number of row and column.

"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        row,col = len(grid),len(grid[0])

        if grid[0][0] or grid[-1][-1]:
            return -1

        if row == 1 and grid[0][0] == 0:
            return 1

        q = collections.deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        step = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx< row and 0<= ny < col and grid[nx][ny] == 0 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
                        if nx == row-1 and ny == col-1:
                            return step + 1
            step += 1
        return -1
