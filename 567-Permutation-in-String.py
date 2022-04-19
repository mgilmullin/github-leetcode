"""
https://leetcode.com/problems/permutation-in-string/

567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

Explanation
Build a counter map for s1. Iterate the string to check if s2 has permutations of s1.

Time Complexity: O(N).
Space Complexity: O(N).
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1)
        
        s1_len = len(s1)
        
        for i in range(len(s2) - s1_len + 1):
            if collections.Counter(s2[i:i+s1_len]) == s1_counter:
                return True
            
        return False 
