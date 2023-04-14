class Solution:
    def distance(self, arr: List[int]) -> List[int]:
        loc = defaultdict(list)
        for i, x in enumerate(arr): loc[x].append(i)
        
        for k, idx in loc.items(): 
            prefix = list(accumulate(idx, initial=0))
            vals = []
            for i, x in enumerate(idx): 
                vals.append(prefix[-1] - prefix[i] - prefix[i+1] - (len(idx)-2*i-1)*x)
            loc[k] = deque(vals)
        
        return [loc[x].popleft() for x in arr]