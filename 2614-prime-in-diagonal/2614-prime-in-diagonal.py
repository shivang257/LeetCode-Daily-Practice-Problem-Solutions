from math import sqrt
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def prime(n):
            if n==1 or n==0:
                return False
            if n>1:
                for i in range(2, int(sqrt(n)) + 1):
                    if (n % i == 0):
                        return False
                return True
        l=[]
        for i in range(len(nums)):
            l.append(nums[i][i])
            l.append(nums[i][len(nums)-1-i])
        l.sort(reverse=True)
        for i in range(len(l)):
            if prime(l[i]):
                return l[i]
        return 0