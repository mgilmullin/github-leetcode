"""
https://leetcode.com/problems/decode-ways/

91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters 
using the reverse of the mapping above (there may be multiple ways).
 
For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' 
since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
 

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero 
("6" is different from "06").
 

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Methodology: Dynamic Programming.
Each combination of the number must be in range 1 and 26 inclusive, 
so that means for each combination, it has to be 1 digit or 2 digits.

Before we find the pattern, there are some special case need to consider.  
If the combination is less than 1 it is invalid. 
If it is greater than 26, we can not find the matched letter for that, 
so we can only split it to 2 and 7. 
For 0, there are only two case will be valid, 10 and 20.

Now we find the base case (with valid number)
If there is only 1 digit, then there is only 1 combination. 
The base case will be: dp[0]=1.
If the last digit is not ‘0’, then there are at least dp[i-1] ways. 

Now, we check last two digits. If the last two digit is in greater than 
‘09’ and smaller than ‘27’, we will add the total ways of step before the last step.
Leading ‘0’ will return 0.
Consective ‘0’ will return 0.

Complexity analisis:
We iterate all dp array, it will cost O(n+1), 
each value will add up last two value as result, 
it will cost (1+2), in total will be O((n+1)+2(n+1)). 
BigO is O(n).

"""

class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if int(s[i-1]) != 0:
                dp[i] = dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]
