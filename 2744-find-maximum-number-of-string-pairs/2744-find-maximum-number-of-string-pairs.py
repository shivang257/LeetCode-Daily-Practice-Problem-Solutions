class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        l=[sorted(i) for i in words]
        a=[]
        res=0
        for i in l:
            if i in a:
                res+=1
            a.append(i)
        return res