"""
https://leetcode.com/problems/combinations/

77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
1 <= n <= 20
1 <= k <= n

Explanation
Use backtracking approach to build all possible combinations.

Time Complexity: O(N).
Space Complexity: O(N).
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        nums = [i for i in range(1, n + 1)]
        
        self.helper(nums, k, results, [], 0)
                
        return results
        
    def helper(self, nums, k, results, combination, start):
        if len(combination) == k:
            results.append(list(combination))
            return
        
        for i in range(start, len(nums)):
            num = nums[i]
            
            combination.append(num)
            self.helper(nums, k, results, combination, i + 1)
            combination.pop()
