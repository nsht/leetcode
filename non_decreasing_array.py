"""
 Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000]. 
"""
import pdb



class Solution:
    def checkPossibility(self, nums):
        is_modified = False
        prev_value = None
        nums2 = []
        if len(nums) == 1 or nums == sorted(nums):
            return True
        for index,value in enumerate(nums):
            if index+1 == len(nums):
                continue
            if prev_value is None:
                if value > nums[index+1]:
                    is_modified = True
                    value = nums[index+1]
            elif value > nums[index+1]:
                if is_modified:
                    return False
                is_modified = True
                if prev_value == value:
                    nums[index+1] = value
                elif prev_value > nums[index+1]:
                    nums[index+1] = value
                else:
                    value = prev_value
                    if nums[index+1] < value:
                        return False
                
            prev_value = value
        return True








# # inp = [3,4,2,3]
print(Solution().checkPossibility([3,4,2,3])) #false
print(Solution().checkPossibility([4,2,3])) #True
print(Solution().checkPossibility([1,5,4,6,7,10,8,9])) #false
print(Solution().checkPossibility([2,3,3,2,4])) #true
print(Solution().checkPossibility([1,2,4,5,3])) #true
print(Solution().checkPossibility([-1,4,2,3])) #true
