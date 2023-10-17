import collections
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        for left, right in zip(leftChild, rightChild):
            if left > -1: indegree[left] += 1
            if right > -1: indegree[right] += 1
            if indegree[left] > 1 or indegree[right] > 1: return False
        queue = collections.deque(i for i, d in enumerate(indegree) if d == 0)
        if len(queue) > 1: return False
        while queue:
            node = queue.popleft()
            for child in leftChild[node], rightChild[node]:
                if child == -1: continue
                indegree[child] -= 1
                if indegree[child] == 0: queue.append(child)
        return sum(indegree) == 0