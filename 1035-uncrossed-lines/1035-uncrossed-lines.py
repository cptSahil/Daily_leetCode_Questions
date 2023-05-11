class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        dp = [0]*(len(nums2)+1)
        for i in range(1,len(nums1)+1):
            prev = cur = 0
            for j in range(1,len(nums2)+1):
                cur = dp[j]
                if nums1[i-1]==nums2[j-1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j],dp[j-1])
                prev = cur
        return dp[len(nums2)]