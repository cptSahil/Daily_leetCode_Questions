class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = k
        count = collections.Counter(answerKey[:k])
        
        left = 0
        for i in range(k,len(answerKey)):
            count[answerKey[i]] += 1
            
            while min(count['T'],count['F'])>k:
                count[answerKey[left]] -= 1
                left += 1
                
            max_size = max(max_size,i - left + 1)
            
        return max_size
    
    
        