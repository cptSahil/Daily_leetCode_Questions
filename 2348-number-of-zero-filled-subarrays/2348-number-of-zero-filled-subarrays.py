class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        start = subarrays = 0
        for end in range(len(nums)):
            if nums[end]:
                start = end + 1
            subarrays += end - start + 1
        return subarrays