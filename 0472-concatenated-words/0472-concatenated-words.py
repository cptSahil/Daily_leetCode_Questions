class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        res = []
        
        for word in words:
            length = len(word)
            dp = [False]*(length+1)
            dp[0] = True
            
            for i in range(1,length+1):
                for j in range((i==length) and 1 or 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in dictionary
            
            if dp[length]:
                res.append(word)
        
        return res