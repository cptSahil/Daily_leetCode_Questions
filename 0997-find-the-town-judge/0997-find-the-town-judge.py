class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return 1
        
        count = [0]*(n+1)
        for i in trust:
            count[i[0]]-=1
            count[i[1]]+=1
            
        for i in range(len(count)):
            if(count[i]==n-1):
                return i
        return -1
    
    
     