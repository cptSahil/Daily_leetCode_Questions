class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = -prices[0]
        s = 0
        s2 = 0 # s[i - 2]
        for i in range(1, len(prices)):
            b = max(b, s2 - prices[i])
            s2 = s
            s = max(s, b + prices[i])
        return s