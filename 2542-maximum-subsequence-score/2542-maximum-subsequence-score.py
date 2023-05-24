class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        min_heap = [0]
        running_sum = 0
        max_score = 0
        for i,(num1, min_in_nums2) in enumerate(nums):
            running_sum += num1
            heappush(min_heap, num1)
            if len(min_heap) > k:
                running_sum -= heappop(min_heap)
                max_score = max(max_score, running_sum * min_in_nums2)
        return max_score