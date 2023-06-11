class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            t=s[i:]+s[:i]
            if t==goal:
                return True
        return False