class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
            res=math.inf
            nums.sort()
            ans=0
            for i in range(len(nums)):
                start=i+1
                end=len(nums)-1
                while start<end:
                    currsum=nums[start]+nums[end]+nums[i]
                    if currsum==target:
                        return target
                    elif abs(currsum-target)<(res):
                        res=abs(currsum-target)
                        ans=currsum
                    if currsum>target:
                        end-=1
                    else:
                        start+=1
            return ans