class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        max_len = 0
        zero = 0
        left, right = 0,0
        while right < len(A):
            zero += 1 - A[right]
            right += 1
            if zero > K:
                zero -= 1 -A[left]
                left += 1
            max_len = max(max_len, right-left)
        return max_len