from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(ptr1, ptr2):
            if ptr1 == len(text1) or ptr2 == len(text2):
                return 0
            
            # Case 1
            if text1[ptr1] == text2[ptr2]:
                return 1 + memo_solve(ptr1+1, ptr2+1)
        
            # Case 2
            else:     
                return max(memo_solve(ptr1+1, ptr2), memo_solve(ptr1,ptr2+1))
                       # ^    # ^ Case 2 - Option 1           ^ Case 2 - Option 2
					   # | __You want the max() result from resulting branches in the tree 
        return memo_solve(0,0)