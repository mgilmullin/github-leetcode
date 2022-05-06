"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

Method: Sliding window. 
If two words are anagrams, then their number of letters is the same. 
We create two dictionaries d1,d2 to record the frequency of letters.
Move s, add the last letter to d2 each time, and check both whether the two dictionaries are the same. 
After checking, remove the first letters.

Time: O(n)
Space: O(n)

"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # variant 1 for small p:
#         from itertools import permutations
#         from re import finditer
        
#         result = []
#         if len(p) <= len(s):
#             permutations = itertools.permutations(p)

#             for item in permutations:
#                 anagram = "".join(item)
#                 overlappedGroups = finditer(r'(?=({}))'.format(anagram), s)

#                 for group in overlappedGroups:
#                     result.append(group.span(1)[0])

#         return list(set(result))

        # variant 2 with slide windows:


        res = []
        d1 = collections.Counter(p)
        window = s[:len(p)-1]
        d2 = collections.Counter(window)
        for start in range(len(s)-len(p)+1):
            end = start + len(p)-1            
            d2[s[end]] = d2.get(s[end], 0) + 1
            if d1 == d2:
                res.append(start)
            # delete the start char
            d2[s[start]] -= 1
            if d2[s[start]]==0:
                del d2[s[start]]
                
        return res

