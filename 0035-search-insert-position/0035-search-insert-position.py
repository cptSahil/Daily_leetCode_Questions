class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums)-1
        # while left<=right:
        #     if nums[left]>target:
        #         return left
        #     if nums[right]<target:
        #         return right+1
        #     mid = left + (right - left)//2
        #     if target==nums[mid]:
        #         return mid
        #     elif target<nums[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid+1
        
        low = 0 
        high = len(nums)-1
        
        while(low<=high):
            mid = low + (high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return low
            
        
        
            