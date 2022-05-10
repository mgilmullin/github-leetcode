"""
https://leetcode.com/problems/permutations-ii/

47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

Method: Backtracking to find permutations. 
The difference between this Permutations II and all Permutations is that this problem has duplicate values. 
So we should skip the element by position not by value when building permutations. 
Also if the permutation has been found, we don’t need to add them to the final result list.

Time Complexity: O(N).
Space Complexity: O(N).

"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        results = []
        
        visited = set()
        self.helper(results, nums, [], visited)
        
        return results
    
    def helper(self, results, nums, permutation, visited):
        if len(permutation) == len(nums):
            if permutation not in results:
                results.append(list(permutation))
            return
        
        
        for i in range(len(nums)):
            if i in visited:
                continue

            permutation.append(nums[i])
            visited.add(i)

            self.helper(results, nums, permutation, visited)

            permutation.pop()
            visited.remove(i)
