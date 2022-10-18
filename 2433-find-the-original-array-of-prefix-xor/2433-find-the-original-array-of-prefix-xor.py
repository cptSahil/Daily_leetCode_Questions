class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = []
        result.append(pref[0])
        for i in range(len(pref)-1):
            result.append(pref[i]^pref[i+1])
        return result