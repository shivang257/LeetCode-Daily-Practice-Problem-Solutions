class Solution:
    def largestGoodInteger(self, num):
        result = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                result = max(result, int(num[i]))
        return "" if result == -1 else str(result) * 3