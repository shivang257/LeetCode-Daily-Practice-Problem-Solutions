class Solution:
    def reverseVowels(self, s: str) -> str:
        vo=[]
        ind=[]
        for i,j in enumerate(s):
            if j in 'AEIOUaeiou':
                vo.append(j)
                ind.append(i)
        vo=vo[::-1]
        l=[i for i in s]
        print(l)
        for i in range(len(ind)):
            print(ind[i])
            l[ind[i]]=vo[i]
        str=''
        for i in l:
            str+=i
        return str