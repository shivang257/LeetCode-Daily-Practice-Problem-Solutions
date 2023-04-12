class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res=[]
        
        def back(start,comb):
            if len(comb)==len(nums):
                res.append(comb[:])
                return
            for i in range(2):
                comb.append(i)
                back(i+1,comb)
                comb.pop()
        back(0,[])
        l=[]
        for i in range(len(res)):
            s=''
            for j in (res[i]):
                s+=str(j)
            if s:
                l.append(s)
        for i in l:
            if i not in nums:
                return i