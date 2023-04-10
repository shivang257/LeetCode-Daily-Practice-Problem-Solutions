class Solution:
    def isValid(self, s: str) -> bool:
        dic={'[':']','(':')','{':'}',0:None}
        stack=[0]
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if dic[stack.pop()]!=i:
                    return False
        return stack==[0]