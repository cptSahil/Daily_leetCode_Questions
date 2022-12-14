class Solution:
    def rob(self, nums: List[int]) -> int:
        # if(len(nums)<3):
        #     return max(nums)
        # for i in range(2,len(nums)):
        #     nums[i]+=max(nums[:i-1])
        # return max(nums)
        
        n = len(nums)
        p1,p2 = 0 , 0
        
        for i in range(n):
            res = max(p1+nums[i],p2)
            p1 = p2 
            p2 = res
        return res