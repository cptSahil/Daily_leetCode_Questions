class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*k
        
        for i in range(1,n+1):
            highest = currMax = 0
            for j in range(1,min(k,i)+1):
                currMax = max(currMax,arr[i-j])
                highest = max(highest, dp[(i-j)%k]+currMax*j)
            dp[i%k] = highest
        return dp[n%k]