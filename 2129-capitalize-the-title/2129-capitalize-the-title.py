class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = []
        for i in title.split(" "):
            i = i.lower()
            if len(i)>2:
                i =i[0].upper()+i[1:]
            s.append(i)
        return " ".join(s)