class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        def clearBit(x, k):
            return ~(1 << k) & x

        @lru_cache(None)
        def dp(mask):  # return (minimum number of work sessions needed, remainTime)
            if mask == 0: return (0, 0)

            ans = n
            ansRemainTime = 0
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = clearBit(mask, i)
                    cntSession, remainTime = dp(newMask)
                    if tasks[i] <= remainTime:  # Consume remainTime of the current session
                        remainTime = remainTime - tasks[i]
                    else:  # Create new session
                        cntSession += 1
                        remainTime = sessionTime - tasks[i]
                    if cntSession < ans or cntSession == ans and remainTime > ansRemainTime:
                        ans = cntSession
                        ansRemainTime = remainTime

            return ans, ansRemainTime

        return dp((1 << n) - 1)[0]