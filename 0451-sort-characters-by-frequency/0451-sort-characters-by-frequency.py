class Solution:
    def frequencySort(self, s: str) -> str:
        a=Counter(s).most_common()
        l=''
        for i in range(len(a)):
            l+=(a[i][0])*a[i][1]
        return l