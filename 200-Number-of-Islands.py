"""
https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


This problem can be solved by method Depth First Search.

To find the number of islands, we need to move from left top to bottom right. For each move we can go up (y-1) or right (x+1) or down (y-1) or left (x-1) directions. After each move, if we are out of the bondary or we find water or we repeat the path then we return to last move and change to another direction to move until we find 1 island. After we find island, we update the count and start to find another island.

BigO
We iterate each cell will cost O(m*n) where m*n is the size of the 2D list. 

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def findIsland(x,y):
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1' and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    findIsland(nx,ny)
            
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1' and (x,y) not in visited:
                    count +=1
                    visited.add((x,y))
                    findIsland(x,y)         
        return count
