"""
https://leetcode.com/problems/integer-break/

343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2, 
and maximize the product of those integers.

Return the maximum product you can get.
 

Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:
2 <= n <= 58

Method: Dynamic Programming. Math. 
The  number 2 can only be split into 1+1. The product is 1.
The number 3 can be split into 2+1 or 1+1+1.  The max product is 2.
The number 4 is divided into 2+2. The product is the largest, which is 4.
The number 5 is divided into 3+2, and the product is the largest, which is 6.
The number 6 is divided into 3+3, and the product is the largest, which is 9.
The number 7 is divided into 3+4, and the product is the largest, which is 12.
The number 8 is divided into 3+3+2, and the product is the largest, which is 18.
The number 9 is divided into 3+3+3, and the product is the largest, which is 27.
The number 10 is divided into 3+3+4, and the product is the largest, which is 36.
Starting from 5, all numbers need to be divided into 3 first, until the remaining number is 2 or 4, 
because the remaining 4 does not need to be divided again: 
divided into two 2 and not splitting are meaningless, 
and 4 can't split a 3 to leave a 1, which will be smaller than the product of splitting 2+2. 
We can start the loop when n is greater than 7. 
We multiply the result by 3, according to the previous Analysis. 

Time complexity: O(n).

"""


class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in range(7, n+1):
            dp.append(dp[i-3] * 3)
        return dp[n]
