class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []
        for i in spells:
            left = 0
            right = n
            while left < right:
                mid = (left + right)//2
                if potions[mid] * i < success:
                    left = mid + 1
                else:
                    right = mid
            res.append(n - left)
        return res