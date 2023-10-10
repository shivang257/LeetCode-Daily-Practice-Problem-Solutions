class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from bisect import bisect_right
        
        nums.sort()
        duplicates = [0 for _ in nums]
        seen = set()
        cur = 0
        for i,num in enumerate(nums):
            cur += num in seen
            seen.add(num)
            duplicates[i] = cur
        duplicates.append(duplicates[-1])
        
        ret = float('inf')
        i = 0
        j = bisect_right(nums, nums[i] + len(nums) - 1)
        while i < len(nums):
            start = nums[i]
            end = start + len(nums) - 1
            
            while j < len(nums) and nums[j] <= end:
                j += 1
            right = len(nums) - j
            left = i
            dupes = duplicates[j] - duplicates[i]
            
            ret = min(ret, left + dupes + right)
            i += 1
        return ret