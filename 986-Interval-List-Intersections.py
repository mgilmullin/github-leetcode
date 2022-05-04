"""
https://leetcode.com/problems/interval-list-intersections/

986. Interval List Intersections

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
 

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1

We use two pointers, i and j, to  manage "discarding" firstList[0] or secondList[0] repeatedly.

Complexity Analysis

Time Complexity: O(M+N), where M,N are the lengths of lists respectively.

Space Complexity: O(M + N), the maximum size of the answer.
"""


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Let's check if firstList[i] intersects secondList[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                res.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1

            else:
                j += 1

        return res
