class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        x_len = len(M)
        y_len = len(M[0]) if x_len else 0
        res = deepcopy(M)
        for x in range(x_len):
            for y in range(y_len):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < x_len and 0 <= _y < y_len
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res