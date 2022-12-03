class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        maxFreq = max(freq.values())
        buckets = [[] for _ in range(maxFreq+1)]
        for c,f in freq.items():
            buckets[f].append(c)
        res = []
        for f in reversed(range(maxFreq+1)):
            for c in buckets[f]:
                res.append(c * f)
                
        return "".join(res)