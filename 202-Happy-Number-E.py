"""
https://leetcode.com/problems/happy-number/

202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
 

Example 1:
Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 2**31 - 1

Method: Hash Table. 
We expect continually following links to end in one of three ways:
1) It eventually gets to 11.
2) It eventually gets stuck in a cycle.
3) It keeps going higher and higher.

We know that any cycles must contain numbers smaller than 243, as anything bigger could not be cycled back to. 
With such small numbers, it's not difficult to write a brute force program that finds all the cycles.
If you do this, you'll find there's only one cycle: 4→16→37→58→89→145→42→20→4. 
All other numbers are on chains that lead into this cycle, or on chains that lead into 1.
We can hardcode a HashSet containing these numbers, and if we ever reach one of them. 
Then we know we're in the cycle. 
There's no need to keep track of where we've been previously.

Complexity Analysis:

Time complexity : O(logn). 

Space complexity : O(1). 
We are not maintaining any history of numbers we've seen. 
The hardcoded HashSet is of a constant size.

"""


class Solution:
    def isHappy(self, n: int) -> bool:

        isCycle = {4, 16, 37, 58, 89, 145, 42, 20}

        def getNext(number):
            totalSum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                totalSum += digit ** 2
            return totalSum

        while n != 1 and n not in isCycle:
            n = getNext(n)

        return n == 1

