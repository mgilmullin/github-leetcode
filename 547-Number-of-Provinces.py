"""
https://leetcode.com/problems/number-of-provinces/

547. Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
 

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

Method: Depth first search

Traverse all cities. For each city, if the city has not been visited yet, then start the depth-first search from the city, through the matrix isConnected obtains which cities are directly connected to the city. 
These cities and the city belong to the same connected component. 
Then continue the depth-first search for these cities until all cities of the same connected component are visited, you can get a province . 
After traversing all cities, you can get the total number of connected components, that is, the total number of provinces.

Time Complexity
Since we are traversing through the entire matrix once, the time complexity is O(N²).

Space Complexity
Space complexity is O(N²) since we are storing all the cities in a set.

"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i: int):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
        
        return circles



