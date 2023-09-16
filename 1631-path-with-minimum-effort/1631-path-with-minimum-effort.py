class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [0, 1, 0, -1, 0]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue  # this is an outdated version -> skip it
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))