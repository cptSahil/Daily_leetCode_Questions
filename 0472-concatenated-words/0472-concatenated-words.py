class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # DP
#         dictionary = set(words)
#         res = []
        
#         for word in words:
#             length = len(word)
#             dp = [False]*(length+1)
#             dp[0] = True
            
#             for i in range(1,length+1):
#                 for j in range((i==length) and 1 or 0, i):
#                     if not dp[i]:
#                         dp[i] = dp[j] and word[j:i] in dictionary
            
#             if dp[length]:
#                 res.append(word)
        
#         return res

        # DFS
        dictionary = set(words)
        res = []
        for word in words:
            visited = [False]*len(word)
            if self.dfs(word,0,visited,dictionary):
                res.append(word)
        return res
    
    def dfs(self,word: str, length: int, visited: List[bool], dictionary:set)->bool:
        if length == len(word):
            return True
        if visited[length]:
            return False
        visited[length] = True
        for i in range(len(word)-(1 if length==0 else 0), length,-1):
            if word[length:i] in dictionary and self.dfs(word,i,visited,dictionary):
                return True
        return False