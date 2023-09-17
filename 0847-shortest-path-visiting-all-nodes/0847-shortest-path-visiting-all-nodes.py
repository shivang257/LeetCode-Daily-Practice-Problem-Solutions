class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """ O(2^N * N^2)T O(2^N * N)S """
        if len(graph) == 1:
            return 0

        nodes = list(range(len(graph)))
        level, seen = collections.deque((n, 0, frozenset(nodes) - {n}) for n in nodes), set((n, frozenset(nodes) - {n}) for n in nodes)

        while level:
            node, deep, stay = level.popleft()
            for kid in graph[node]:
                if not (stay_ := stay - {kid}): 
                    return deep + 1
                if (kid, stay_) not in seen:
                    seen.add((kid, stay_)), level.append((kid, deep + 1, stay_))