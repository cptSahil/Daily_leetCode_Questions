class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        res = count
        
        
        for i in range(k,len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            res = max(res, count)
        return res