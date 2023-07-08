class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pair = [0]*(n-1)
        for i in range(n-1):
            pair[i] = weights[i] + weights[i+1]
        pair.sort()
        
        answer = 0
        for i in range(k-1):
            answer += pair[n-2-i] - pair[i]
        return answer