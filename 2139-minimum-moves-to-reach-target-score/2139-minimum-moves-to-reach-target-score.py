class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result=0
        while target>1 and maxDoubles:
            if target%2:
                target-=1
            else:
                maxDoubles-=1
                target=target//2
            result+=1
        return result+target-1