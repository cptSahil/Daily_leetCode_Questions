class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l = []
        
        for i in range(26):
            l.append(False)
            
        for i in sentence.lower():
            if not i == ' ':
                l[ord(i) - ord('a')] = True
                
        for char in l:
            if char == False:
                return False
        return True
            