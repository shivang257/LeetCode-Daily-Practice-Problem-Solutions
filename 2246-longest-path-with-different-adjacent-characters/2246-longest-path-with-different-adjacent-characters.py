class Solution:
    def longestPath(self, parent, s):
        children = [[] for i in range(len(s))]
        for i,j in enumerate(parent):
            if j >= 0:
                children[j].append(i)
        
        res = [0]
        def dfs(i):
            candi = [0]
            for j in children[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    candi.append(cur)
                    
            candi = nlargest(2, candi)
            res[0] = max(res[0], sum(candi) + 1)
            return max(candi) + 1
        
        dfs(0)
        return res[0]