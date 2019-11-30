"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


"""
import pdb


# TODO Try setting temp_water_trapped using prev node
class Solution:
    def trap(self, height):
        trapped_water = 0
        max_left = 0
        max_right = 0
        for index,he in enumerate(height):
            max_left = max(height[:index],default=0)
            max_right = max(height[index:],default=0)
            min_height = min([max_left,max_right],default=0)
            if he < min_height:
                trapped_water += (min_height-he)
        return trapped_water


(()())(())(()(()))
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,3]
output = Solution().trap(height)
print(output)
# twt 1
# sn 1