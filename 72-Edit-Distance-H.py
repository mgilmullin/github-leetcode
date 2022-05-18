"""
https://leetcode.com/problems/edit-distance/

72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

Method: Dynamic Programming (dp)
There are several cases:

1) word1[i] == word2[j]
There is no need to change, so  dp[i + 1][j + 1] = dp[i][j]

2) word1[i] != word2[j]
We are going to use one of those three operations ：

insert = dp[i][j + 1], represents the inserting of a character;
delete = dp[i + 1][j]， represents deleting a character;
replace = dp[i, j]， represents replacing of a character.
and then:
dp[i + 1][j + 1] = min(insert, delete, replace) + 1

Time complexity: O(m * n), m = len(word1), n = len(word2)

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i][j]
                    dp[i + 1][j + 1] = min(insert, delete, replace) + 1
        return dp[m][n]
