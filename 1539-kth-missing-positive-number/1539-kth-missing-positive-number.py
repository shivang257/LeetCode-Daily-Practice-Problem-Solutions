class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[]
        arr.sort()
        arr=set(arr)
        m=range(1,10**5)
        for i in m:
            if i not in arr:
                l.append(i)
            if len(l)==k:
                break
        return l[-1]