"""
https://leetcode.com/problems/subsets-ii/

90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

Method^
A typical backtracking coding problem.

We can have a recursion function to add visited subsets to the final results (Power Set). Remember to make a deep copy whenever we are adding the subset to the results.

Time Complexity: O(n)
Space Complexity: O(n)

"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        powerSet = []
        nums = sorted(nums)

        self.helper(powerSet, [], 0, nums)
        
        return powerSet
    
    def helper(self, powerSet, combination, start, nums):
        if combination not in powerSet:
            powerSet.append(list(combination))
        
        for i in range(start, len(nums)):
            combination.append(nums[i])            
            self.helper(powerSet, combination, i + 1, nums)            
            combination.pop()

