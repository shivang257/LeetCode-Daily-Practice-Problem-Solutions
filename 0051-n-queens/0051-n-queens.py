class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        def backtrack(queens,posDia,negDia):
            p=len(queens)
            if len(queens)==n:
                res.append(queens)
                return
            for c in range(n):
                if c not in queens and p-c not in negDia and p+c not in posDia:
                    backtrack(queens+[c],posDia+[p+c],negDia+[p-c])
        backtrack([],[],[])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in sol] for sol in res]