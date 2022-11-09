class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        c, s = 1, self.stack
        while s and s[-1][0]<= price:
            c += s.pop()[1]
        s.append((price,c))
        return c

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)