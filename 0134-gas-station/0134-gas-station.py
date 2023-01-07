class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n,total,surplus=len(gas),0,0
        start=0
        for i in range(n):
            total+=gas[i]-cost[i]
            surplus+=gas[i]-cost[i]
            if surplus<0:
                surplus=0
                start=i+1
        return -1 if total<0 else start