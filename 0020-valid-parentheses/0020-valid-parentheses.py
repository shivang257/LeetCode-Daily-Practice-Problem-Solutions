class Solution:
    def isValid(self, s: str) -> bool:
        stack=[0]
        dic = {0:None,"[":"]","{":"}","(":")"}
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if dic[stack.pop()]!=i:
                    return False
        return stack==[0]