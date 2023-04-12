class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for i in path.split('/'):
            if i == ".." and res:
                res.pop()
            elif i not in "..":
                res.append(i)
        return '/'+'/'.join(res)