"""
https://leetcode.com/problems/combination-sum-ii/

40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

Method: Backtracking.
In this problem, each number in the input is not unique. The implication of this difference is that we need some mechanism to avoid generating duplicate combinations.

In this problem, each number can be used only once. The implication of this difference is that once a number is chosen as a candidate in the combination, it will not appear again as a candidate later.

We implement the backtracking process with the function named 
backtrack(comb, remain, curr, results).

Complexity Analysis:
Let N be the size of the input array.
Time Complexity: O(2**N).
Space Complexity: O(N).

"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                # make a copy of the resulted combination
                results.append(list(comb))
                return

            for nextCurr in range(curr, len(candidates)):

                if nextCurr > curr \
                  and candidates[nextCurr] == candidates[nextCurr-1]:
                    continue

                pick = candidates[nextCurr]
                # optimization: skip the rest of elements starting from 'curr' index
                if remain - pick < 0:
                    break

                comb.append(pick)
                backtrack(comb, remain - pick, nextCurr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results
