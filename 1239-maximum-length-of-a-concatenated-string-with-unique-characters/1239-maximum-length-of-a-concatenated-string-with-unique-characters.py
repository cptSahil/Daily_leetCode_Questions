class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = []
        for i in arr:
            u = set(i)
            if len(u) == len(i):
                unique.append(u)
        
        concatenate = [set()]
        for i in unique:
            for c in concatenate:
                if not c & i:
                    concatenate.append(c | i)
        return max(len(i) for i in concatenate)
    
        