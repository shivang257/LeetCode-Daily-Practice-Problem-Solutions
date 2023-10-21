class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = deque()
        max_queue = deque()
        max_sum = float('-inf')

        for i in range(len(nums)):
            window.append(nums[i])
            if max_queue:
                window[-1] += max_queue[0]

            max_sum = max(max_sum, window[-1])

            while max_queue and window[-1] > max_queue[-1]:
                max_queue.pop()
            if window[-1] > 0:
                max_queue.append(window[-1])
            if i >= k:
                if max_queue and window[0] == max_queue[0]:
                    max_queue.popleft()
                window.popleft()

        return max_sum