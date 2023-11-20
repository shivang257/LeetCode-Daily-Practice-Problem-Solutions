class Solution(object):
    def garbageCollection(self, garbage, travel):
        n = len(garbage)
        ans = 0

        for i in range(n - 1):
            ans += 3 * travel[i]

        for s in garbage:
            ans += len(s)

        for i in range(n - 1, 0, -1):
            if "G" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        for i in range(n - 1, 0, -1):
            if "P" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        for i in range(n - 1, 0, -1):
            if "M" not in garbage[i]:
                ans -= travel[i - 1]
            else:
                break

        return ans