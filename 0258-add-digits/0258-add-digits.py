class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=0
            while num:
                s+= num%10
                num=num//10
            num=s
        return num