class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        res=[]
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def back(i,comb):
            if len(comb)==n:
                res.append(comb)
                return
            for c in dic[digits[i]]:
                back(i+1,comb+c)
        if digits=="":
            return []
        back(0,"")
        return res