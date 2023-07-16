class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            cur_skill = 0
            for skill in p:
                if skill in skill_index:
                    cur_skill |= 1 << skill_index[skill]
            for prev, need in dict(dp).items():
                comb = prev | cur_skill
                if comb == prev: continue
                if comb not in dp or len(dp[comb]) > len(need) + 1:
                    dp[comb] = need + [i]
        return dp[(1 << n) - 1]