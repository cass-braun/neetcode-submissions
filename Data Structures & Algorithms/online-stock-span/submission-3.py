class StockSpanner:
    def __init__(self):
        # Stack stores tuples of: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # While stack is not empty and the top price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the popped element to our current span
            span += self.stack.pop()[1]
            
        # Push the current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span
            
       


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)