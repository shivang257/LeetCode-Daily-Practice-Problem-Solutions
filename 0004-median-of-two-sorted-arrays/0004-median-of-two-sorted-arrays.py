class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=len(nums1)+len(nums2)
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if(a%2!=0):
            return nums1[a//2]
        else:
            return (nums1[a//2-1]+nums1[a//2])/2
        
        