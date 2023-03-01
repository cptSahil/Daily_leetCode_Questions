class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0]*len(nums)
        
        def merge(left:int,mid:int,right:int):
            s1 = left
            s2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid
            
            for i in range(n1):
                temp[s1 + i] = nums[s1 + i]
            for i in range(n2):
                temp[s2 + i] = nums[s2 + i]
                
            i, j, k = 0, 0, left
            while i<n1 and j<n2:
                if temp[s1 + i] <= temp[s2+j]:
                    nums[k] = temp[s1 + i]
                    i += 1
                else:
                    nums[k] = temp[s2 + j]
                    j += 1
                k += 1
            
            while i < n1:
                nums[k] = temp[s1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp[s2 + j]
                j += 1
                k += 1
        
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left,mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)
        merge_sort(0,len(nums) - 1)
        return nums
            