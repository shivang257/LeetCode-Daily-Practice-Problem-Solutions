import heapq

class Solution:

    def findMaximizedCapital(self, k, w, profits, capital):
        projects = [(c, p) for c, p in zip(capital, profits)]
        projects.sort()
        
        available_projects = []
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(available_projects, -projects[i][1])
                i += 1
            if not available_projects:
                break
            w -= heapq.heappop(available_projects)
            k -= 1
        
        return w