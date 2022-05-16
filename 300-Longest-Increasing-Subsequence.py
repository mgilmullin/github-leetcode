"""
https://leetcode.com/problems/longest-increasing-subsequence/

300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
 

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Method: Dynamic Programming.
There may be more than one LIS combination, it is only necessary for us to return the length.

We must to creat a dp list to memorize the length of increasing subsequence. 
If the current element is greater than prevous element, then current length of increasing 
subsequence is the previous length of increasing subsequence + 1. 
Then we return the max length in dp list.

Init each element of dp list to 1 as there is at least 1 number of increasing subsequence 
unless the input is empty list.
If the current element is greater than prevous element, then current length of increasing 
subsequence is the previous length of increasing subsequence + 1.
Once the current element is greater than the max element of previous, 
there is no need to compare more previous elements.

For answer:
Return the max element of dp list.

Complexity:
dp list will cost O(n).   The iterated dp list will cost ((n-1)**2). 
In total will be O((n-1)**2+n).
BigO: O(n**2)

"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums: return 0
        L = len(nums)
        dp=[1]*L
        preMax = nums[0]
        for i in range(1,L):
            preMax = nums[i-1] if nums[i-1]>preMax else preMax
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    if nums[j] == preMax:
                        dp[i] = max(dp[i],dp[j]+1)
                        break
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
