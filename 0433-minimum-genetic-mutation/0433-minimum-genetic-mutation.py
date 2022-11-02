class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        q=deque([(start,0)])
        while q:
            curr,mut=q.popleft()
            if curr==end:
                return mut
            
            for i in range(8):
                for ch in "ACGT":
                    n=curr[:i]+ch+curr[i+1:]
                    
                    if n in bank:
                        bank.remove(n)
                        q.append((n,mut+1))
        return -1