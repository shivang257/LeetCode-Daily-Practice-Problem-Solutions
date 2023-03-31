class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,int(num**0.5)+1):
            if i*i == num:
                return True
            if i*i>num:
                return False