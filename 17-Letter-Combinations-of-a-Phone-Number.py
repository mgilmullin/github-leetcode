"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


Methodology: Depth-First Search (DFS). Recursion.
Since each digit can possibly mean one of several characters, we'll need to create code that branches down the different paths as we iterate through the input digit string (digits).

This quite obviously calls for a Depth-First Search (DFS) approach as we will check each permutation of characters and store them in our answer array (ans). For a DFS approach we can use one of several options, but a recursive solution is generally the cleanest.

But first, we'll need to set up a lookup table (lookTab) to convert a digit to its possible characters. Since the digits are actually low-indexed integers, we can actually choose between an array or map/dictionary here with little difference.

For our DFS function (dfs), we'll have to feed it the current position (pos) in digits as well as the string (str) being built. The function will also need to have access to digits, lookTab, and ans.

The DFS function itself is  simple. It will push a completed str onto ans, otherwise it will look up the characters that match the current pos, and then fire off new recursive functions down each of those paths.

Once we're done, we should be ready to return ans.

"""



lookTab = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lenDigits, ans = len(digits), []
        if digits == "": return []
        def bfs(pos: int, st: str):
            if pos == lenDigits: ans.append(st)
            else:
                letters = lookTab[digits[pos]]
                for letter in letters:
                    bfs(pos+1,st+letter)
        bfs(0,"")
        return ans
