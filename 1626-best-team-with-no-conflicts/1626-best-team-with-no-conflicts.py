class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        scores = [s for a,s in sorted(zip(ages, scores))]
        dp = scores[:]
        max_scores = 0
        for curr in range(N):
            for prev in range(curr):
                if scores[prev] <= scores[curr]:
                    dp[curr] = max(dp[curr], dp[prev]+ scores[curr])
            
            max_scores = max(max_scores, dp[curr])
        return max_scores
    
    # Time Complexity = O(NlogN+NlogK)
    # Space Complexity = O(N+K)