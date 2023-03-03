class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        to_find = hash(needle)
        needle_len = len(needle)
        for ind in range(len(haystack)):
            if hash(haystack[ind: ind + needle_len]) == to_find:
                return ind
            
        return -1