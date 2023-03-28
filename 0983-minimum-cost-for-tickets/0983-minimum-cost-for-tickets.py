class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         res  = 0
#         last7 = deque()
#         last30 = deque()
        
#         for cost in days:
#             while last7 and last7[0][0]+7<=cost:
#                 last7.popleft()
#             while last30 and last30[0][0]+30<=cost:
#                 last30.popleft()
#             last7.append([cost,res+costs[1]])
#             last30.append([cost,res+costs[2]])
#             res = min(res+costs[0],last7[0][1],last30[0][1])
#         return res
        
        dp = [0]*(days[-1]+1)
        days = set(days)
        for i in range(1,len(dp)):
            if i in days:
                dp[i] = min(dp[max(i-1,0)]+costs[0],dp[max(i-7,0)]+costs[1],dp[max(i-30,0)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]