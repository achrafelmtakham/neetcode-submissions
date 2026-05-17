class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - min_so_far
            if price < min_so_far:
                min_so_far = price
            max_profit = max(max_profit, profit)
        return max_profit