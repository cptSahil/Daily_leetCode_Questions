class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}
        
        for i,j in zip(pattern, words):
            if i in charToWord and charToWord[i] != j:
                return False
            if j in wordToChar and wordToChar[j] != i:
                return False
            charToWord[i] = j
            wordToChar[j] = i
        return True
        