"""
https://leetcode.com/problems/3sum/

15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

Analysis:
We have to find such triplets whose sum is zero and there should be no duplicates in the answer.

Approach:
1. Sort the array.
2. For each element i, do the following steps.
3. Set two pointers left — j = i + 1 and right — k = nums.length - 1.
4. Check if nums[i] + nums[j] + nums[k] == 0 and if it is zero, add these three numbers to the resultant list.
5. If the sum nums[i] + nums[j] + nums[k] < 0, this means we can move left pointer forward because since the array is sorted and the sum is less than zero, therefore, it makes sense to check for greater value to make the sum bigger.
6. If the sum nums[i] + nums[j] + nums[k] > 0, this means we are too right and can move the right pointer backward because since the array is sorted and the sum is greater than zero, therefore, it makes sense to check for smaller value to make the sum lesser.
7. In between loops, we also need to make sure that we are not checking for duplicate values.

Time Complexity:
We are scanning the entire array keeping one element fixed. We are doing this for every element in the array. Thus, we are scanning each element of array n number of times. And we are doing this for n times, hence the worst case time complexity will be O(n**2 + n * log n) which comes down to O(n**2).

Space Complexity:
We are not using any data structure for the intermediate computations, hence the space complexity is O(1).
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the given array
        nums.sort()
        # Length of the array
        n = len(nums)
        # Resultant list
        triplets = list()
        # Loop for each character in the array
        for i in range(0, n):
            # Avoid duplicates due to i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Left and right pointers
            j = i + 1
            k = n - 1
            # Loop for remaining pairs
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Avoid duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
