class Solution:
    def predictPartyVictory(self, senate):
        A = collections.deque()
        people = [0, 0]
        bans = [0, 0]

        for person in senate:
            x = person == 'R'
            people[x] += 1
            A.append(x)

        while all(people):
            x = A.popleft()
            people[x] -= 1
            if bans[x]:
                bans[x] -= 1
            else:
                bans[x^1] += 1
                A.append(x)
                people[x] += 1

        return "Radiant" if people[1] else "Dire"