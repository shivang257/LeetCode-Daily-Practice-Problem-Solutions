class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums).most_common(k)
        l=[]
        for i in range(len(a)):
            l.append(a[i][0])
        return l