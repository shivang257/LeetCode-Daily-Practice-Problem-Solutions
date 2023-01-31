class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
      
        max_scores=[0]*(max(ages)+1)
        
        for score, age in sorted(zip(scores, ages)): max_scores[age] = score + max(max_scores[:age + 1])

        return max(max_scores)