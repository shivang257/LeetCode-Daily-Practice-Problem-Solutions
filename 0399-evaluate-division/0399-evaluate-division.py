class Solution:
    
    def answer(self, current, end, scalar):
        if current==end: return scalar
        self.visited.add(current)
        if current in self.graph:
            for i in self.graph[current]:
                if i[0] not in self.visited:
                    a=self.answer(i[0],end,scalar*i[1])
                    if a!=-1: return a
        return -1
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph,self.visited={},set()
        for i in range(len(equations)):
            if equations[i][0] not in self.graph:
                self.graph[equations[i][0]]=[]
            if equations[i][1] not in self.graph:
                self.graph[equations[i][1]]=[]
            self.graph[equations[i][0]].append((equations[i][1],1/values[i]))
            self.graph[equations[i][1]].append((equations[i][0],values[i]))
        v=[]
        for i in queries:
            self.visited=set()
            if i[0] not in self.graph or i[1] not in self.graph:
                v.append(-1)
                continue
            v.append(1/self.answer(i[0],i[1],1) if i[0]!=i[1] else 1)
        return v