"""
https://leetcode.com/problems/max-points-on-a-line/

149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.


Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:
1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.

Method: Hash Table.
We search the maximum number of points on a line passing through the point i. 
N is the number of points. 
Save these lines is a hash table with a counter 2. 
If the line is horizontal, i.e. y = c, 
one could use this constant c as a line key in a hash table of horizontal lines.
The other lines could be represented as y = slope * x + c.
A slope value is sufficient to represent a unique line starting from a specific point i.
We could use a pair of co-prime integers to represent unique slope.

Algorithm:
1) Initiate the maximum number of points maxCount = 1.
2) Iterate over all points i from 0 to N - 2.
3) For each point i find a maximum number of points maxPointsOnI(i) on a line passing through the point i :
Initiate the maximum number of points on a line passing through the point i : count = 1.
Iterate over next points j from i + 1 to N - 1.
If j is a duplicate of i, update a number of duplicates for point i.
If not:
Save the line passing through the points i and j.
Update count at each step.
Return maxPointsOnI(i) = count + duplicates.
4) Update the result maxCount = max(maxCount, maxPointsOnI(i))


Complexity Analysis:

Time complexity : O(N**2) 
since we draw not more than N - 1 lines passing through the point 0, not more than N - 2 lines for the point 1, 
and the only one line for the point N - 2. That results in N(N - 1)/2 operations, i.e. O(N**2 ) time complexity.

Space complexity : O(N) to track down not more than N - 1 lines.

"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def maxPointsOnI(i):

            def slopeCoprime(x1, y1, x2, y2):
                dx, dy = x1 - x2, y1 - y2
                if dx == 0:   
                    return (0, 0)
                elif dy == 0:  
                    return (sys.maxsize, sys.maxsize)
                elif dx < 0:
                  
                    dx, dy = - dx, - dy
                gcd = math.gcd(dx, dy)
                slope = (dx / gcd, dy / gcd)
                return slope

            def addLine(i, j, count, duplicates):

                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                
                if x1 == x2 and y1 == y2:  
                    duplicates += 1
                
                elif y1 == y2:
                    nonlocal horLines
                    horLines += 1
                    count = max(horLines, count)
                else:
                    slope = slopeCoprime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)
                return count, duplicates
            
            lines, horLines = {}, 1

            count = 1
            duplicates = 0
            for j in range(i + 1, n):
                count, duplicates = addLine(i, j, count, duplicates)
            return count + duplicates
            
        n = len(points)
        if n < 3:
            return n
        
        maxCount = 1
        for i in range(n - 1):
            maxCount = max(maxPointsOnI(i), maxCount)
        return maxCount
