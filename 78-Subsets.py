"""
https://leetcode.com/problems/subsets/

78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique

Method: Cascading
Start from empty subset in output list. 
At each step one takes new integer into consideration and generates new subsets from the existing ones.

Complexity Analysis:
Time complexity: O(n*(2**n)) 
To generate all subsets and then copy them into output list.

Space complexity: O(n*(2**n))
This is the number of solutions for subsets multiplied by the number n of elements to keep for each subset.

For a given number, it could be present or absent (i.e. binary choice) in a subset solution. As as result, for n numbers, we would have in total 2**n choices.

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        powerSet = [[]]
        
        for num in nums:
            powerSet += [current + [num] for current in powerSet]
        
        return powerSet
