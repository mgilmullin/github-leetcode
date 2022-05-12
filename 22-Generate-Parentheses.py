"""
https://leetcode.com/problems/generate-parentheses/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8

"""


class Solution:
    def __init__(self):
        self.result = []  

    def bracketsGenerator(self, n: int, line="", leftBrackets=0, rightBrackets=0) -> None:
        if leftBrackets == n and rightBrackets == n:
            self.result.append(line)  

        else:
            if leftBrackets < n:
                self.bracketsGenerator(n, line + "(", leftBrackets + 1, rightBrackets)

            if rightBrackets < leftBrackets:
                self.bracketsGenerator(n, line + ")", leftBrackets, rightBrackets + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.bracketsGenerator(n)
        return self.result
