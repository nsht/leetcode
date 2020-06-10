class Solution:
    def searchInsert(self, nums, target) -> int:
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            return nums.index(target)

import bisect
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            bisect.insort(nums,target)
            return nums.index(target)
        

        
print(Solution().searchInsert([1,3,5,6],5) == 2)
