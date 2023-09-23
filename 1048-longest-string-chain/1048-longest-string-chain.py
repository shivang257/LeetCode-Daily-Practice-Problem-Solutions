class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        result = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    result = max(result, dp[word])

        return result