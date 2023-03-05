class Solution(object):
    def minJumps(self, arr):
        if len(arr) == 1: return 0  # obviously

        adj = defaultdict(list)
        for i, n in enumerate(arr):
            adj[n].append(i)

        ans = [0] * len(arr)  # the return value is ans[0], once we find it, we can return immediately.
        dq = deque([len(arr) - 1])  # obviously, ans[-1] == 0, so we fill in ans from ans[-1] to ans[0] iteratively

        while dq:
            i = dq.popleft()

            # move forward if the next one has not seen before that is ans[i + 1] == 0
            # note that the ans[len(arr) - 1] is always 0, we should NOT update it, so i < len(arr) - 1
            if i < len(arr) - 2 and ans[i + 1] == 0:
                ans[i + 1] = ans[i] + 1
                dq.append(i + 1)

            # move backward if the previous one has not seen before that is ans[i - 1] == 0
            if i > 0 and ans[i - 1] == 0:
                ans[i - 1] = ans[i] + 1
                if i - 1 == 0: return ans[0]
                dq.append(i - 1)

            # move to j where arr[i] == arr[j]
            for j in adj[arr[i]]:
                if ans[j] == 0 and j < len(arr) - 1:
                    ans[j] = ans[i] + 1
                    if j == 0: return ans[0]
                    dq.append(j)
            adj.pop(arr[i])