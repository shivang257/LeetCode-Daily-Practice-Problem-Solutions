class Solution:
    def trap(self, height: List[int]) -> int:
        l,h,mx,leftmax,rightmax=0,len(height)-1,0,0,0
        while l<=h:
            leftmax=max(leftmax,height[l])
            rightmax=max(rightmax,height[h])
            if leftmax<rightmax:
                mx+=(leftmax-height[l])
                l+=1
            else:
                mx+=(rightmax-height[h])
                h-=1
        return mx