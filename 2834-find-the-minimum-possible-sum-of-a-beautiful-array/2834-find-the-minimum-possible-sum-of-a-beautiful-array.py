class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        seen=set()
        i=1
        while len(seen)<n:
            if target-i not in seen:
                seen.add(i)
            i+=1
        return sum(seen)