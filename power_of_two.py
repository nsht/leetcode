import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return (math.ceil(self.log2(n)) == math.floor(self.log2(n)))
    
    def log2(self,x):
        return (math.log10(x)/math.log10(2))

print(Solution().isPowerOfTwo(16))

