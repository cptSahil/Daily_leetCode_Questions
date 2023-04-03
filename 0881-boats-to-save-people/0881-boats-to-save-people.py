class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b = 0
        start = 0
        end = len(people)-1
        people.sort()
        while start<end:
            if people[start]+people[end]<=limit:
                start+=1
            # else:
            #     start = 0
            end-=1
            b+=1
        return b+int(start==end)