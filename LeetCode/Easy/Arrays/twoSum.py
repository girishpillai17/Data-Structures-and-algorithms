from typing import List

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

nums =  [2,7,11,15]
target = 26

#solution 1 --> Brute Force
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

#print(twoSum(nums,target))



# solution 2 --> HashMap Approach
def twoSum_hashMap(nums, target):
    dict = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in dict:
            return [dict[compliment], i]
        dict[nums[i]] = i

#print(twoSum_hashMap(nums,target))
