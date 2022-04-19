"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Hint:
We can find the set of only unique elements of the datatype using the set() function in python. 
As we travel through the string in the loop, there are only two possibilities: the given character in the string is either part of the longest substring or it is not. How do we determine that? If that character already appeared in the substring we are building, we break it there and store the length till that point and start a new substring from that character.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):  # Checking if the string is unique
            return len(s)
        substring = ''
        maxLen = 1
        for char in s:
            if char not in substring:  # If given character is not in substring we are generating, we add it to the substring
                substring = substring + char
                maxLen = max(maxLen, len(substring))  # We update the maxlength if our substring is longer than the current max.
            else:  # Else, if the character is already part of the substring, we need to break the flow
                substring = substring.split(char)[1] + char # And create a new substring from that point onwards and this new substring is build from the next character. Process repeats till the loop ends.
        return maxLen
