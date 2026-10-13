class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100000
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                # Calculate profit if we sold today, and update max_profit if it's a record
                current_profit = price - min_price
                max_profit = max(max_profit, current_profit)
                
        return max_profit