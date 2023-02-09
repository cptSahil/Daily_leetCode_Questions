class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        grp = [set() for i in range(26)]
        for idea in ideas:
            grp[ord(idea[0])-ord('a')].add(idea[1:])
            
        res = 0
        
        for i in range(25):
            for j in range(i+1,26):
                mutual = len(grp[i] & grp[j])
                res += 2*(len(grp[i])-mutual)*(len(grp[j])-mutual)
        return res