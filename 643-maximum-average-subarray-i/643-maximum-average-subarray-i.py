class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1 = 0
        mx = -10000
        i = 0
        j = 0
        while(j<len(nums)):
            sum1 = sum1+nums[j]
            if(j-i+1<k):
                j+=1
            elif (j-i+1==k):
                avg = sum1/k
                mx = max(mx,avg)
                sum1 = sum1-nums[i]
                i+=1
                j+=1
        return mx
                
            