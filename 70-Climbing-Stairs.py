"""
https://leetcode.com/problems/climbing-stairs/

70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Note:
Given n will be a positive integer.

Methodology
This question solved by Dynamic Programming.

Find the base case
When climb 1 stair, we need 1 step
when climb 2 stairs, we need 2 steps which 1+1 or 2
when climb 3 stairs, we need 3 steps which 1+1+1, 1+2, 2+1
when climb 4 stairs, we need 5 steps which 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 …. The base case will be:
dp[1]=1,
dp[2]=2,
dp[3]=3,
dp[4]=5

To reach the current stairs for example (stair 4), we can easily add 1 step from last stair (stair 3) and that will give us 1+1+1+1, 1+2+1, 2+1+1. Or we can easily add 2 steps from the one before last stair (stair 2) and that will give us 1+1+2 and 2+2. Since we can only move 1 or 2 steps each time. We do not need more previous stairs. So we get answer 5 in total.

"""

def climbStairs(self, n: int) -> int:
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]


# class Solution:
#     def climbStairs(self, n):
       
#        if n == 0 or n == 1 or n == 2 or n == 3:
#             return n
#         else:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)
