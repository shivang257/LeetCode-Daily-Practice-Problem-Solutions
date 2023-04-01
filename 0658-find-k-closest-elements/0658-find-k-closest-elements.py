class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        left,right=0,n-k-1
        while left<=right:
            mid=(left+right)//2
            if x>(arr[mid]+arr[mid+k])//2:
                left=mid+1
            else:
                right=mid-1
        return arr[left:left+k]