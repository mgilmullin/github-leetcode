"""
https://leetcode.com/problems/max-area-of-island/

695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

Intuition and Algorithm
We want to know the area of each connected shape in the grid, then take the maximum of these.
If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use visit to keep track of squares we haven't visited before. It will also prevent us from counting the same shape more than once.

Complexity Analysis
Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.

Space complexity: O(R*C), the space used by seen to keep track of visited squares, and the space used by the call stack during our recursion.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in visit and grid[r][c]):
                return 0
            visit.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) +
                    area(r, c - 1) + area(r, c + 1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))   
