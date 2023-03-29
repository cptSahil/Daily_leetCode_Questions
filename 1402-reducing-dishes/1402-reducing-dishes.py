class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        v = satisfaction.sort(reverse = True)
        n = len(satisfaction)
        pre_sum , res = 0, 0
        for i in range(n):
            pre_sum += satisfaction[i]
            if pre_sum < 0:
                break
            res += pre_sum
        return res