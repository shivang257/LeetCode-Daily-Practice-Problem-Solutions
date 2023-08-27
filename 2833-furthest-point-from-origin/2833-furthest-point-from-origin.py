class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l=moves.count("L")
        r=moves.count("R")
        if l>=r:
            for i in moves:
                if i=="_":
                    l+=1
        else:
            for i in moves:
                if i=="_":
                    r+=1
        return abs(l-r)