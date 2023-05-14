class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        vis = [0] * (n + 1)
        vis[1] = 1
        p = 1
        for i in range(1, n + 1):
            p = (p + k * i) % n
            if p == 0:
                p = n
            if vis[p] == 1:
                break
            vis[p] = 1
        return [i for i in range(1, n + 1) if vis[i] == 0]