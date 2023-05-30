class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        left,right,top,bottom=0,m-1,0,n-1
        ans=[]
        while left<=right and top<=bottom:
            for col in range(left,right+1):
                ans.append(matrix[top][col])
            top+=1
            for row in range(top,bottom+1):
                ans.append(matrix[row][right])
            right-=1
            for col in range(right,left-1,-1):
                ans.append(matrix[bottom][col])
            bottom-=1
            for row in range(bottom,top-1,-1):
                ans.append(matrix[row][left])
            left+=1
        return ans[:m*n]