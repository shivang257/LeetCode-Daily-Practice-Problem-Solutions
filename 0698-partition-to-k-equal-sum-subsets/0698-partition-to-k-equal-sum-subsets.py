class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)//k
        nums.sort(reverse=True)
        sums=[0]*k
        n=len(nums)
        if sum(nums)%k!=0:
            return False
        def backtrack(i):
            if i==n:
                return len(set(sums))==1
            for j in range(k):
                if sums[j]<=total:
                    sums[j]+=nums[i]
                if sums[j]<=total and backtrack(i+1):
                    return True
                sums[j]-=nums[i]
                if sums[j]==0:
                    break
            return False
        return backtrack(0)