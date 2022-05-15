"""
https://leetcode.com/problems/word-break/

139. Word Break

Given a string s and a dictionary of strings wordDict, return true 
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Methodology: Dynamic Programming.
Create a dp list to indicate each word start character position and end position 
(end position is one step more than the position of end character).
dp[0] = True

Find the pattern:
Go throught the string character by character. 
Use the previous characters to form words. 
Check if those words are in dictionary. 
If so, we mark the next position of the word as True to indicate that before this True mark, 
there is word that appear in dictionary. 
In the meanwhile, the True mark will also be the start character for next word.
Result:
the last value in dp list indicate if all characters are used out to form dictionary’s word.

Time Complexity:
We iterate all dp array, it will cost O(n+1), each value will iterate all it’s previous value, 
it will cost ((n+1)*(n+1-1)), in total will be O(n**2+n). 
BigO: O(n**2)

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    print(s[j:i])
                    dp[i] = True
        return dp[-1]
