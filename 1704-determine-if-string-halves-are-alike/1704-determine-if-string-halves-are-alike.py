class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        first_half = 0
        second_half = 0
        
        mid = (len(s)//2) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for index, char in enumerate(s):
            if char in vowels:
                if index<=mid:
                    first_half += 1
                else:
                    second_half += 1
        return first_half == second_half
            