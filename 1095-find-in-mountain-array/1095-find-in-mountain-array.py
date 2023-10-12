class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        leng = mountain_arr.length()
        left, right = 0, leng-1
        while left < right:
            mid = (left+right) // 2
            if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                right = mid
            else:
                left = mid + 1 
        peak = left
        if target == mountain_arr.get(peak):
            return peak

        l, r = 0, peak-1
        while l <= r: 
            print(l, r, end =' ')
            mid = (l + r) // 2
            print('1:', mid)
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                r = mid - 1
            else:
                l = mid + 1
                
        l, r = peak+1, leng-1
        while l <= r:
            print('2:', mid)
            mid = (l + r) // 2
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1