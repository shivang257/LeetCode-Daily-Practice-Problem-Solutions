class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(2,len(arr)):
            if arr[i-2]%2 and arr[i-1]%2 and arr[i]%2:
                return True
        return False