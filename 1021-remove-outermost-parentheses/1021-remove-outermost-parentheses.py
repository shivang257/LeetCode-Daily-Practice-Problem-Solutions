class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened=0
        res=''
        for i in s:
            if i=='(' and opened >0:
                res+=i
            if i==')' and opened>1:
                res+=i
            opened+=1 if i=='(' else -1
        return res