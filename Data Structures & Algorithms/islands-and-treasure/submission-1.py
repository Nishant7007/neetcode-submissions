from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if(grid[i][j]!=0):
                    continue
                visited = [[False]*n for i in range(m)]
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while(queue):
                    # print(queue)
                    p, q = queue.popleft()
                    neighbors = [(p+1, q), (p-1, q), (p,q-1), (p, q+1)]
                    for x, y in neighbors:
                        # print(p, q, x, y)
                        # print(visited)
                        # print(grid)
                        if(x>=0 and x<m and y>=0 and y<n and visited[x][y]==False and grid[x][y]!=0 and grid[x][y]!=-1 and grid[x][y]>grid[p][q]+1):
                            # print(x, y)
                            grid[x][y] = min(grid[x][y], grid[p][q]+1)
                            queue.append((x, y))
                            visited[x][y] = True