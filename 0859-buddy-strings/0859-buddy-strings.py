class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        difference = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                difference += 1
        if difference == 2:
            return Counter(goal) == Counter(s)
        elif difference == 0:
            return not len(set(goal)) == len(goal)
        else:
            return False