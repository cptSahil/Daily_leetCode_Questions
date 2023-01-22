class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==0:
            return [[]]
        def loops(res,temp,s):
            if len(s)==0:
                res.append(list(temp))
                return
            
            for i in range(1,len(s)+1):
                if s[:i] == s[:i][::-1]:
                    loops(res,temp+[s[:i]],s[i:])
        
        res = []
        loops(res,[],s)
        
        return res