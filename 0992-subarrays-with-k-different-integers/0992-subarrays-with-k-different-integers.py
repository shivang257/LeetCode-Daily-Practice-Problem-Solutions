class Solution:
    def atmost(self,nums,k):
        l=0
        mp=defaultdict(int)
        res=0
        for r in range(len(nums)):
            mp[nums[r]]+=1
            while len(mp)>k:
                mp[nums[l]]-=1
                if mp[nums[l]]==0:
                    mp.pop(nums[l])
                l+=1
            res+=r-l+1
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums,k)-self.atmost(nums,k-1)