class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        return [candies[i]+extraCandies>=m for i in range(len(candies))]