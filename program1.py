class Solution: 
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid or not grid[0]:
            return 0
        
        def dfs(x, y):
            
            
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 'W' or visited[x][y]:
                return
           
           
            visited[x][y] = True
            
            
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    # Found an unvisited land cell, start DFS and count this island
                    dfs(i, j)
                    island_count += 1
        
        return island_count           