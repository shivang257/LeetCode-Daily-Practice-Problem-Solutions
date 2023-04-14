class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique=[""]
        c=0
        for a in arr:
            for i in unique:
                x=a+i
                if len(x)==len(set(x)):
                    unique.append(x)
                    c=max(len(x),c)
        return c