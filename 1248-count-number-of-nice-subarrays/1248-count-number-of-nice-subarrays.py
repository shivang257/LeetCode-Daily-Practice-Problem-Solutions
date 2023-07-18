class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]=nums[i]%2
        mp=defaultdict(int)
        mp[0]=1
        res=0
        psum=0
        for i in nums:
            psum+=i
            res+=mp[psum-k]
            mp[psum]+=1
        return res