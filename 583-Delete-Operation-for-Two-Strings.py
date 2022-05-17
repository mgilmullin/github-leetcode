"""
https://leetcode.com/problems/delete-operation-for-two-strings/

583. Delete Operation for Two Strings

Given two strings word1 and word2, return the minimum number of steps 
required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
 

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.

Method: Dynamic Programming
The problem is asking us to identify the longest common subsequence (LCS) between the two words 
(word1, word2). The answer wi

For a typical LCS solution, we would use a dynamic programming (dp) approach and 
use nested loops to compare each letter of each word against each other (word1[i], word2[j]). 
This would normally call for a dp array of size (L1 + 1) * (L2 + 1), where L1 =word1.length 
and L2 = word2.length. Since the LCS process references the previous row and column 
for the target cell, we'll need the extra buffer of 0-filled cells. 
Each cell in the dp array at dp[i][j] will represent the longest subsequence found between 
word1.substr(0,i) and word2.susbtr(0,j). 
Our final answer will then be dp[L1][L2].

Since the dp array is being built iteratively, we can reduce the normal space complexity 
from  O(L1 * L2) by only keeping the current and last rows (dpCurr, dpLast) as we iterate through.
This will drop the space complexity to O(N). Doing this, we can also ensure that the shorter 
word is used for N by swapping the two words if necessary.

Time Complexity: O(L1 * L2) where L1 and L2 are the lengths of the two words.
Space Complexity: O(N) where N is the length of the smaller of the two words/

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        L1, L2 = len(word1), len(word2)
        if L1 < L2: word1, word2, L1, L2 = word2, word1, L2, L1
        dpLast, dpCurr = [0] * (L2 + 1), [0] * (L2 + 1)
        for c1 in word1:
            for j in range(L2):
                dpCurr[j+1] = dpLast[j] + 1 if c1 == word2[j] else max(dpCurr[j], dpLast[j+1])
            dpLast, dpCurr = dpCurr, dpLast
        return L1 + L2 - 2 * dpLast[L2]
