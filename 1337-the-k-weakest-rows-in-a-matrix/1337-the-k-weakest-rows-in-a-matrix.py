class Solution:
	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
		m = len(mat)
		rows = sorted(range(m), key=lambda i: (mat[i], i))
		del rows[k:]
		return rows