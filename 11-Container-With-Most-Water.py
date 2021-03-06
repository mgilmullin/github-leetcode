"""
https://leetcode.com/problems/container-with-most-water/

11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Methodology:
We use two pointers to solve this question. First we set left pointer which is the start of the list and right pointer which is the end of the list. 
We compare the area of the container that made by left and right to the max area. If the current area is larger than the max area, we update the max area to the current area. We will move the pointer with shorter height closer to the other pointer until two pointer get touched.

BigO:
Total time complexity is O(n).
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left,right =0, len(height)-1
        result = 0
        
        while left < right:
            water = (right-left) * min(height[left], height[right])
            if water > result:
                result = water
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return result
