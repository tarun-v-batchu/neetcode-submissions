class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        traverse = []

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :

                if grid[i][j] == 0 :
                    traverse += [(i, j)]
        
        distance = 1
        i = 0
        distance_len = len(traverse)
        
        while i < len(traverse) :

            x, y = traverse[i]
            if x > 0 and grid[x-1][y] == 2147483647:
                grid[x-1][y] = distance
                traverse += [(x-1, y)]
            if x < len(grid) - 1 and grid[x+1][y] == 2147483647:
                grid[x+1][y] = distance
                traverse += [(x+1, y)]
            if y > 0 and grid[x][y-1] == 2147483647:
                grid[x][y-1] = distance
                traverse += [(x, y-1)]
            if y < len(grid[0]) - 1 and grid[x][y+1] == 2147483647:
                grid[x][y+1] = distance
                traverse += [(x, y+1)]


            i += 1
            if i == distance_len :
                distance += 1
                distance_len = len(traverse)
        
        # return grid
                
            


