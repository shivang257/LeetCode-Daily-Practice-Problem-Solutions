from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        match = 0
        
        for i in range(len(s2)):
            # Add right
            if s2[i] in s1_map:
                s1_map[ s2[i] ] -= 1
                if s1_map[ s2[i] ] == 0: match += 1
            
            # Subtract left
            if i+1 > len(s1):
                if (left:=s2[i-len(s1)]) in s1_map:
                    s1_map[left] += 1
                    # means it came to 1 from 0
                    if s1_map[ left ] == 1: match -= 1
            
            if match == len(s1_map):
                return True

        return False