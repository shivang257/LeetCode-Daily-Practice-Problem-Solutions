class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while len(str(num))>1:
            num=str(num)
            for i in num:
                s+=int(i)
            if len(str(s))==1:
                return int(s)
            num=int(s)
            s=0
        return num