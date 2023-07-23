class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        stack=[]
        mapp={}
        for n in nums2:
            while stack and n>stack[-1]:
                mapp[stack.pop()]=n
            stack.append(n)
        while stack:
            mapp[stack.pop()]=-1
        for n in nums1:
            res.append(mapp[n])
        return res