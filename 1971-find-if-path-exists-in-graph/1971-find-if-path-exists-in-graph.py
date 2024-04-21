class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
            
        q = deque([start])
        seen = set([start])
        while q:
            node = q.popleft()            
            if node == end:
                return True            
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
                
        return False