class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
        s=0
        c=0
        for i in range(1,n-1):
            s+=salary[i]
            c+=1
        return s/c