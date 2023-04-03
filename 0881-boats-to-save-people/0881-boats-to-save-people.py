class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        lo,hi=0,len(people)-1
        while lo<=hi:
            if people[lo]+people[hi]<=limit:
                lo+=1
                hi-=1
            else:
                hi-=1
            count+=1
        return count