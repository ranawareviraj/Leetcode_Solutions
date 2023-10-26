class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_buy_price = math.inf

        for sale_price in prices:
            prev_buy_price = min(prev_buy_price, sale_price)
            profit += (sale_price - prev_buy_price)
            prev_buy_price = sale_price
        
        return profit
        