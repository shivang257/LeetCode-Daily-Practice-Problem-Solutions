class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        diff1, diff2 = -1, -1
        A_letters = set()
        for i in range(len(A)):
            if A[i] != B[i]:
                if diff1 == -1:
                    diff1 = i
                elif diff2 == -1:
                    diff2 = i
                else:
                    return False 
            A_letters.add(A[i])
        if diff1 != -1 and diff2 != -1: 
            return A[diff1] == B[diff2] and A[diff2] == B[diff1]
        if diff1 != -1: 
            return False
        return len(A_letters) < len(A) 