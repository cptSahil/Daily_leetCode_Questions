class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = [0]*26
        for letter in p:
            target[ord(letter)-ord('a')] += 1
        count = [0]*26
        left = right = 0
        res = []
        while right < len(s):
            count[ord(s[right])-ord('a')] += 1
            if right-left == len(p):
                count[ord(s[left])-ord('a')] -= 1
                left += 1
            if count == target:
                res.append(left)
            right += 1
        return res