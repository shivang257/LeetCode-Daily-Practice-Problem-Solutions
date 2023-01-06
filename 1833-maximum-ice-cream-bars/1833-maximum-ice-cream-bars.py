class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        a=0
        costs.sort()
        i=0
        while coins>=0 and i<len(costs):
            coins-=costs[i]
            if coins<0:
                break
            i+=1
            a+=1
        return a