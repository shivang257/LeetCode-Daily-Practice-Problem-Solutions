import math
class Solution(object):
    def arrangeCoins(self, n):
        rows=1
        while n>0:
            rows+=1
            n-=rows
        return rows-1