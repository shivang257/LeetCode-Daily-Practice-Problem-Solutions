class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c=defaultdict(int)
        c[0]=1
        res=0
        psum=0
        for i in nums:
            psum+=i
            res+=c[psum-goal]
            c[psum]+=1
        return res