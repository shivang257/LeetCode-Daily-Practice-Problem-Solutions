class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque([(start, 0)])
        
        while q:
            curr_gene, mutations = q.popleft()
            
            if curr_gene == end:
                return mutations
            
            for i in range(8):
                for ch in "ACGT":
                    next_gene = curr_gene[:i] + ch + curr_gene[i+1:]
                    
                    if next_gene in bank:
                        bank.remove(next_gene)
                        q.append((next_gene, mutations + 1))    
        
        return -1