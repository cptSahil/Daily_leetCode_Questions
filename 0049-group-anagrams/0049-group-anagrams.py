class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            key = ''.join(sorted(list(i)))
            if key in d.keys():
                d[key].append(i)
            else:
                d[key]=[i]
        return [item for item in d.values()]