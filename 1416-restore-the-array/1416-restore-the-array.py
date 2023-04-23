class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        #Bottom-up
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1
        
        for i in reversed(range(n)):
            if s[i] == '0':
                continue
            ways = 0
            num = 0
            for j in range(i,n):
                num  = num * 10 + ord(s[j]) - ord('0')
                if num <= k:
                    ways += dp[j+1]
                else:
                    break
                
            dp[i] = ways % (10**9+7)
        return dp[0]