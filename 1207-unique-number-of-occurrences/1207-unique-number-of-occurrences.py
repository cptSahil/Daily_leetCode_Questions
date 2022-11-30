class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        v=c.values()
        if len(v)==len(set(v)):
            return True 
        else:
            return False