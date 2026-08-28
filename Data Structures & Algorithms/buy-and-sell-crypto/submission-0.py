class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        # Output: 6 (Explanation: Buy prices[1] i.e. 1 and sell prices[4] i.e. 7, profit = 7 - 1 = 6)
        # See graph in video for Hint

        l = 0 # Buy day
        r = 1 # sell day
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]: # if sell > bought
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r = r + 1

        return max_profit
            