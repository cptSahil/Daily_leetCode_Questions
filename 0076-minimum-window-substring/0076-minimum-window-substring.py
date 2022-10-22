class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if n<len(t):
            return ""
        mp = [0]*256
        
        start = 0
        res = n+1
        c = 0
        
        for i in t:
            mp[ord(i)]+=1
            if mp[ord(i)]==1:
                c+=1
                
        i = 0
        j = 0
        
        while(j<n):
            mp[ord(s[j])]-=1
            if mp[ord(s[j])]==0:
                c-=1
                
                while c==0:
                    if res>j-i+1:
                        
                        res = j-i+1
                        start = i
                        
                    mp[ord(s[i])]+=1
                    if mp[ord(s[i])]>0:
                        c+=1
                    i+=1
            j+=1
        if res>n:
            return ''
        return s[start:start+res]