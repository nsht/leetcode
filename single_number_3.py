class Solution:
    def singleNumber(self, nums):
        elem = {}
        for x in nums:
            if x not in elem:
                elem[x] = 1
            else:
                del elem[x]
        return list(elem)
            

print(Solution().singleNumber([1,2,1,3,2,5]))
	
