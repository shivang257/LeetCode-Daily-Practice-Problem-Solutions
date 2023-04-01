class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        def getOperationsCount(arr: List[int]) -> int:
            sm, n = sum(arr), len(arr)
            mi = inf
            cur = 0
            for i, num in enumerate(sorted(arr)):
                mi = min(mi, (i * num - cur) + ((sm - cur) - (n - i) * num))
                cur += num
            return mi    
        
        gcd = math.gcd(len(arr), k)
        return sum(getOperationsCount(arr[i :: gcd]) for i in range(gcd))