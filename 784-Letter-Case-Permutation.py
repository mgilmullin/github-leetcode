"""
https://leetcode.com/problems/letter-case-permutation/

784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Constraints:
1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.

Explanation
Use the backtracking approach to build permutations. If the character is an alphabetical letter, build permutation in both uppercase or lowercase.

Time Complexity: O(N).
Space Complexity: O(N).
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        
        self.helper(results, s, "", 0)
        
        return results
    
    def helper(self, results, s, permutation, start):
        if len(permutation) == len(s):    
            results.append(permutation)
            return
        
        if s[start].isalpha():
            self.helper(results, s, permutation + s[start].upper(), start + 1)
            self.helper(results, s, permutation + s[start].lower(), start + 1)            
        else:
            self.helper(results, s, permutation + s[start], start + 1)   
