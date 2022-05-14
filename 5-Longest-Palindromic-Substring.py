"""
https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
 

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

Methodology: Dynamic Programming
To find palindromic substring, we need to know the start index and end index 
for each substring. 
The start index and end index will range the substring as outter boundary. 
If the start element and end element are same, then we check if the substring of 
[start index + 1:end index] is palindromic. 
If it is and the current length of substring[start:end+1] is greater than maximum substring
 then we update the maxmium substring. 
Note that, single character is palindromic.

Complexity Analysis:

Time complexity : O(n**2)

Space complexity : O(n**2)

When iterate the whole string, the BigO is O(n) where n is size of the string. 
Each character will need at most n/2 iteration to find if the string block is palindromic. 
So bigO is O(n*n/2) which is O(n**2)

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = '' if not s else s[0]
        maxLen = 1
        size = len(s)
        dp=[[False]*size for _ in range(size)]

        for start in range(size-1,-1,-1):
            dp[start][start]=True

            for end in range(start+1,size):
                if s[start]==s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            longest = s[start: end+ 1]
        return longest
