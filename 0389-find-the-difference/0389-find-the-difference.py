class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(lambda x,y: x ^ y, map(ord,s+t)))
    