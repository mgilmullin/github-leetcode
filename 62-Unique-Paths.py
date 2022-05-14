"""
https://leetcode.com/problems/unique-paths/

62. Unique Paths

There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths 
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways 
to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:
1 <= m, n <= 100

Method: Dynamic Programming.
1. There is only one way to reach the right most edge 
and there is only one way to reach the bottom most edge.
So we init the first row and first column of 2D list with 1.
2. The robot can only move either down or right. 
For each target cell that the robot want to reach, it is either from left cell 
of the tagret or from up cell of the target. Therefore we need sum up target’s 
left cell and up cell to get the total path to reach the target cell. 
When reach to the bottom-right corner, then number in the bottom-right corner 
will be the answer. 

Time Complexity:
Init the first row and first column that will cost O(m+n). 
Then iterate all 2D dp array, it will cost O(m*n). 
In total will cost (m+n+mn). 
So generally, it is O(n**2)

Space Complexity:
O(n**2)

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
