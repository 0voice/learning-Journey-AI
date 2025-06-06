def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    path = []

    def dfs(x, y):
        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or visited[x][y]:
            return False
        path.append((x, y))
        visited[x][y] = True
        if (x, y) == (rows - 1, cols - 1):
            return True
        if dfs(x+1, y) or dfs(x, y+1) or dfs(x-1, y) or dfs(x, y-1):
            return True
        path.pop()
        return False

    if dfs(0, 0):
        print("Path found:", path)
    else:
        print("No path found")
