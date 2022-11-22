class Solution:
    
    # Make dp a class variable :)
    dp = [0]

    def numSquares(self, n: int) -> int:

        dp = self.dp
        
        # Precompute the perfect squares.
        perfectSq = [pow(i,2) for i in range(1, int(sqrt(n))+1)]
        
        # We are building dp up to length n+1.
        while len(dp) < n+1:
            
            # Will add this new element to dp
            dpI = inf
            
            # dp equation
            for ps in perfectSq:
                if len(dp)<ps: break
                dpI = min(dpI,1+dp[-ps])
            
            dp.append(dpI)
        
        return dp[n]