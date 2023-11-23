class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArith(n):
            mx, mn, st = max(n), min(n), set(n)
            if (mx - mn)%(len(n)-1) != 0: return False
            step = (mx - mn)//(len(n)-1)
            if not step: return mx == mn
            for i in range(mn, mx, step):
                if i not in st:
                    return False
            return True       
        res = []
        for i in range(len(l)):
            res.append(isArith(nums[l[i]:r[i]+1]))
        return res