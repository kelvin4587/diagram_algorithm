import heapq
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        row, col = [[] for _ in range(m)], [[] for _ in range(n)]

        def update(x: int, y: int) -> int:
            return y if x == -1 or y < x else x

        for i in range(m):
            for j in range(n):
                while row[i] and row[i][0][1] + grid[i][row[i][0][1]] < j:
                    heapq.heappop(row[i])
                if row[i]:
                    dist[i][j] = update(dist[i][j], dist[i][row[i][0][1]] + 1)

                while col[j] and col[j][0][1] + grid[col[j][0][1]][j] < i:
                    heapq.heappop(col[j])
                if col[j]:
                    dist[i][j] = update(dist[i][j], dist[col[j][0][1]][j] + 1)

                if dist[i][j] != -1:
                    heapq.heappush(row[i], (dist[i][j], j))
                    heapq.heappush(col[j], (dist[i][j], i))
        return dist[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    list1 = [[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]
    print(s.minimumVisitedCells(list1))
    list2 = [[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]
    print(s.minimumVisitedCells(list2))
    list3 = [[2,1,0],[1,0,0]]
    print(s.minimumVisitedCells(list3))
