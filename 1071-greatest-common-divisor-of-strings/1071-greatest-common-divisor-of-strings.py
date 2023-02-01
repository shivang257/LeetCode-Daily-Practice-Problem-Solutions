import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        k=math.gcd(len(str1),len(str2))
        if str1+str2==str2+str1:
            return str2[:k]
        return ""