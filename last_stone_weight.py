class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            shard = stones.pop()-stones.pop()
            if shard !=0:
                stones.append(shard)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

print(Solution().lastStoneWeight([2,7,4,1,8,1]))
