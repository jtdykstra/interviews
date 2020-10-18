class Solution:
    
    def markVisited(self, x, y, grid, visited):
        # if the position is invalid terminate the recursion
        if (x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])):
            # if the node has been visited terminate the recursion
            # if the node is "water" terminate the recursion
            if (not visited.get((x,y), False) and grid[x][y] == '1'):
                visited[(x,y)] = True
                self.markVisited(x-1, y, grid, visited) # left
                self.markVisited(x+1, y, grid, visited) # right
                self.markVisited(x, y+1, grid, visited) # up
                self.markVisited(x, y-1, grid, visited) # down

    def checkIsland(self, x, y, grid, visited):
        # only "count" this island if it hasn't been visited previously
        # and this location is "land"
        if (not visited.get((x,y), False) and grid[x][y] == '1'):
            self.markVisited(x,y,grid,visited)
            return 1
        else:
            return 0

    def numIslands(self, grid):
        total = 0
        visited = {}
        # visit all nodes and do a recursive traversal
        for x, row in enumerate(grid):
            for y, col in enumerate(row):
                total += self.checkIsland(x, y, grid, visited)

        return total
                

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))
print(sol.numIslands(grid2))

