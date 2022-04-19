"""
https://leetcode.com/problems/rotting-oranges/

994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Methodology BFS (breadth-first search):
        Add all fresh oranges to freshSet and append all rotten oranges to rotten_queue.
        Use BFS to find all fresh oranges that adjacent to the current rotten orange, 
        turn these fresh oranges to rotten and remove these from freshSet. In the meantime, track the steps of turning.
        After we finish the turning, if there is still a fresh orange in freshSet, return -1 otherwist return the step.
        We traversal all elements of 2D list once so total time complexity is O(mn) ~ O(n^2)
        where m is size of row and n is size of columns.
        """
        row, col = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        freshSet = set()
        rotten = collections.deque()
        step = 0
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    freshSet.add((x, y))

                elif grid[x][y] == 2:
                    rotten.append([x, y, step])

        while rotten:
            x, y, step = rotten.popleft()

            for dx, dy in dirs:
                if 0 <= x + dx < row and 0 <= y + dy < col and grid[x + dx][y + dy] == 1:
                    grid[x + dx][y + dy] = 2
                    freshSet.remove((x + dx, y + dy))
                    rotten.append([x + dx, y + dy, step + 1])

        return step if not freshSet else -1
