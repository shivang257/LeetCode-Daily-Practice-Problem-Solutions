class Solution:
    def groupThePeople(self, groupSizes):
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]