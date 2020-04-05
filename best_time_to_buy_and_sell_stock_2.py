import pdb
class Solution:
    def maxProfit(self, prices):
        max_len = len(prices) - 1
        max_profit = 0
        buy_price = None
        next_index = None
        for day,price in enumerate(prices):
            if next_index is not None:
                if day != next_index:
                    continue
                else:
                    next_index = None

            next_day = day+1
            if not next_day <= max_len:
                break
            if prices[next_day] < price:
                continue
            buy_price = price
            for d2,p2 in enumerate(prices[next_day:max_len+1]):
                if not next_day+1+d2 <= max_len:
                    if buy_price is not None:
                        max_profit += prices[-1] - buy_price
                        buy_price = None
                        next_index = next_day+d2+1
                    break
                if prices[next_day+d2] > prices[next_day+1+d2]:
                    max_profit += prices[next_day+d2] - buy_price
                    buy_price = None
                    next_index = next_day+d2+1
                    break
        if buy_price is not None:
            max_profit += prices[-1] - buy_price
            buy_price = 0
        return max_profit

print(f"Solution: {Solution().maxProfit([7,1,5,3,6,4])}") # 7
print(Solution().maxProfit([1,2,3,4,5])) # 4
print(Solution().maxProfit([7,6,4,3,1]) == 0) # 0
print(Solution().maxProfit([1,2])) # 1
print(Solution().maxProfit([2,1,2,0,1]))