from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        grid = classroom
        m, n = len(grid), len(grid[0])
        litter = {}
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    sr, sc = i, j
                elif grid[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1
        if k == 0:
            return 0
        target = (1 << k) - 1
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        q = deque([(sr, sc, energy, 0, 0)])
        best[sr][sc][0] = energy
        while q:
            r, c, e, mask, moves = q.popleft()
            if mask == target:
                return moves
            if e == 0:
                continue
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] == 'X':
                    continue
                ne = e - 1
                nm = mask
                if (nr, nc) in litter:
                    nm |= 1 << litter[(nr, nc)]
                if grid[nr][nc] == 'R':
                    ne = energy
                if ne <= best[nr][nc][nm]:
                    continue
                best[nr][nc][nm] = ne
                q.append((nr, nc, ne, nm, moves + 1))
        return -1