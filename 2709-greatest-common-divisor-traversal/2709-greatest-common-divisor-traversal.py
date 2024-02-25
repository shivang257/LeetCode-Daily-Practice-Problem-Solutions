class Graph:
    def __init__(self, n: int):
        self.n = n
        self.edges = [[] for _ in range(n)]
    
    def traverse(self, x: int, visited: List[bool]):
        visited[x] = True
        for y in self.edges[x]:
            if not visited[y]:
                self.traverse(y, visited)
    
    def addEdge(self, x: int, y: int):
        self.edges[x].append(y)
        self.edges[y].append(x)
    
    def isConnected(self) -> bool:
        visited = [False for _ in range(self.n)]
        self.traverse(0, visited)
        return visited.count(True) == self.n


class Solution:
    def getPrimeFactors(self, x: int) -> int:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                while x % i == 0:
                    x //= i
                yield i
        if x != 1:
            yield x
    
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        g = Graph(n)
        seen = {}
        for i in range(n):
            if nums[i] == 1:
                return False
            for prime in self.getPrimeFactors(nums[i]):
                if prime in seen:
                    g.addEdge(i, seen[prime])
                else:
                    seen[prime] = i
        return g.isConnected()