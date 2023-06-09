class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for word in strs:
            l[tuple(sorted(word))].append(word)
        return list(l.values())