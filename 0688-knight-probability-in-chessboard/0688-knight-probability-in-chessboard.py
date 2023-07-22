class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        totalMoves = 8 ** K
        dpArr = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
        return self._getMoves(N, K, r, c, dpArr)/totalMoves
    
    def _getMoves(self, N:int, K:int, r:int, c:int, dpArr: List[List[List]]) -> None:
        if r < 0 or c < 0 or r >= N or c >= N:
            return 0
        if K == 0:
            return 1
        if dpArr[r][c][K]:
            return dpArr[r][c][K]
        places = [[1,2],[1,-2],[-1,2],[-1,-2],[-2,-1],[-2,1],[2,1],[2,-1]]
        res = 0
        for i, j in places:
            res += self._getMoves(N, K-1, r+i, c+j, dpArr)
        dpArr[r][c][K] = res
        return res