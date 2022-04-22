"""
https://leetcode.com/problems/triangle/

120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 
Methodology
This question solved by Dynamic Programming. 

The base case can be original 2D list, we will replace the value of each cell with minimum sum.
To use dynamic programming, we need to sum up each cell with it’s previous adjancent cell.
When reach to the bottom row, then minimum number in the bottom row will be the answer.

BigO
Init the triangle will cost O(m-1). Then iterate all 2D dp array, it will cost O((m-2)*(m-4)). In total will cost (m-1+(m-2)*(m-4)) equal to (m^2-5m+7) so generally is O(n^2).

 """
 
 class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1,m):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1]+=triangle[i-1][-1]
        for i in range(2,m):
            for j in range(1,i):
                triangle[i][j]+=min(triangle[i-1][j-1], triangle[i-1][j])
        print(triangle)
        return min(triangle[-1])