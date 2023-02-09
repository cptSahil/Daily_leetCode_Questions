class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr = 0
        last = 0
        for i in range(len(nums)-1):
            last = max(last,nums[i]+i)
            if(i==curr):
                curr = last
                jumps+=1
        return jumps