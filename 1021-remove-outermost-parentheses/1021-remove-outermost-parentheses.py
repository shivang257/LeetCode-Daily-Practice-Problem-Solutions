class Solution:
    def removeOuterParentheses(self, s):
        res, opened = [], 0
        for c in s:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)