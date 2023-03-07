class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        t = max(time)
        left, right = 1, t*totalTrips
        
        while left<right:
            mid = (left+right)//2
            cost = 0
            for i in range(len(time)):
                cost+= mid//time[i]
            if cost >= totalTrips:
                right = mid
            else:
                left = mid+1
        return left