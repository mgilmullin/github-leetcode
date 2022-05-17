"""
https://leetcode.com/problems/longest-common-subsequence/

1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
 

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Method: Dynamic Programming (dp)
dp[i][j] represents the longest common subsequence between text1[0 : i] and text2[0 : j].

If text1[i] == text2[j], then the longest common subsequence just increase from previous 
position from both words by 1: f[i][j] = f[i – 1][j – 1] + 1.

Otherwise, if text1[i] != text2[j], the longest common subsequence would be the longest 
between text1[i – 1] and text2[j] or text1[i] and text2[j – 1].

Time complexity: O(L1*L2), because we are solving L1*L2 subproblems. 
Solving each subproblem is an O(1)operation.
Space complexity: O(L1*L2). We are allocating a 2D array of size L1*L2 
to save the answers to subproblems.

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        L1 = len(text1)
        L2 = len(text2)
        
        dp = []
        
        for i in range(L1 + 1):
            dp.append([])
            for j in range(L2 + 1):
                dp[i].append(0)
                
        for i in range(L1):
            for j in range(L2):                
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[L1][L2]
