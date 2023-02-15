class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a=''
        for i in num:
            a+=str(i)
        b=int(a)+k
        b=str(b)
        l=[]
        for i in b:
            l.append(int(i))
        return l