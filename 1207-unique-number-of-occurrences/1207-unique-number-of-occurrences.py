class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=Counter(arr).most_common()
        a=[]
        for i in d:
            a.append(i[1])
        return len(a)==len(set(a))