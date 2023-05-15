class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        even, odd = 0, 0
        for i in range(n): 
            if i % 2 == 1 and s[i] == '1': odd += 1
            if i % 2 == 0 and s[i] == '1': even += 1
        
        print(n, even, odd)
        if n % 2 == 0: 
            return min(even + n // 2 - odd, odd + n // 2 - even)
        
        if n % 2 == 1: 
            result = min(even + n // 2 - odd, odd + n // 2 + 1 - even)
            for i in range(n): 
                if s[i] == '1': 
                    even, odd = odd + 1, even - 1
                    result = min(result, min(even + n // 2 - odd, odd + n // 2 + 1 - even))
                else: 
                    even, odd = odd, even
                    result = min(result, min(even + n // 2 - odd, odd + n // 2 + 1 - even))
            return result