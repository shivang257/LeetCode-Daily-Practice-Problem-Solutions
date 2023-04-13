class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        sums = [0]*k
        subsum = sum(nums) // k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False        
        
        return walk(0)