class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row,cols=len(matrix),len(matrix[0])
        l,r=0,row*cols-1
        while l<=r:
            mid=(l+r)//2
            nums=matrix[mid//cols][mid%cols]
            if nums==target:
                return True
            elif nums<target:
                l=mid+1
            else:
                r=mid-1
        return False