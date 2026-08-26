class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, x, y, visited) :
            # print(x, y)
            if visited[x][y] or grid[x][y] == 0:
                return visited, 0
            
            visited[x][y] = True
            count = 0
            if x > 0:
                visited, num = dfs(grid, x - 1, y, visited)
                count += num
            if y > 0 :
                visited, num = dfs(grid, x, y - 1, visited)
                count += num
            if x < len(grid) - 1 :
                visited, num = dfs(grid, x + 1, y, visited)
                count += num
            if y < len(grid[0]) - 1 :
                visited, num = dfs(grid, x, y + 1, visited)
                count += num
            
            return visited, count + 1
        
        maximum = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                # print(i, j)
                visited, area = dfs(grid, i, j, visited)
                maximum = max(maximum, area)
        
        return maximum