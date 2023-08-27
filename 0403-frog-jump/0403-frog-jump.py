class Solution(object):
    def canCross(self, stones):
        stone_set, fail = set(stones), set()
        stack = [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in fail:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            fail.add((stone, jump))
        return False