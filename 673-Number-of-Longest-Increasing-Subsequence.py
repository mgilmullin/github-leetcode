"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

673. Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.
 

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, 
and there are 5 subsequences' length is 1, so output 5.

Constraints:
1 <= nums.length <= 2000
-106 <= nums[i] <= 106

Method: Dynamic Programming.
We need to build connection between length of the longest increasing subsequence and 
the count the of length. 
For that, we need to get current element’s length of longest increasing subsequence and 
meanwhile we also need to know the current element’s count of longest increasing subsequence. 
The answer is sum up each longest increasing subsequence’s count.

We need two dp list here.
One is for the length of the longest increaseing subsequence and each element represent 
the current longest length. 
Another one is for counting the number of such sequence and each element represent 
the count of increasing of include element. length. 
The length is easy to come up. If the current element is greater than before 
(make the subsequence increasing), then we will get the max length of previous plus 1.
Else just stay in 1 (Not increasing). 
The count is hard to understand. 
The current element is the sum of previous longest increasing subsequence 
whose max element is less than current element (this will make the current subsequence 
keep increasing and also means the previous longest increasing subsequences’ length is 1 less 
than the current longest increasing subsequence).
Answer:
Return the value from count that element is bigest element in length.

Time complexity: 
dp list will cost O(2n). 
Iterated  dp list will cost ((n-1)*n). 
In total will be O((n-1)*n+2n). 
BigO: O(n**2).

"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        L = len(nums)
        if L <= 1: return L
        lengths = [1] * L 
        counts = [1] * L 

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = max(lengths[i],lengths[j]+1)
                        counts[i] = counts[j]
                    elif lengths[i]==lengths[j] + 1:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for j, c in enumerate(counts) if lengths[j] == longest)
