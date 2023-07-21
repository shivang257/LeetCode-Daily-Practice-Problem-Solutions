class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_count = collections.Counter(t)
        start, end = 0, 0
        min_window = ''
        target_len = len(t)
        
        for end in range(len(s)):
            if target_count[s[end]] > 0:
                target_len -= 1
                
            target_count[s[end]] -= 1
            #print('Target count',target_count)
            while target_len == 0:
                window_len = end - start + 1
                
                if not min_window or window_len < len(min_window):
                    min_window = s[start:end + 1]
                    
                target_count[s[start]] += 1
                #print('In while target count',target_count)
                if target_count[s[start]] > 0:
                    target_len += 1
                #print('Target length', target_len)
                start += 1
                
        return min_window