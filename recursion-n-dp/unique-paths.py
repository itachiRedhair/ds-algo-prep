class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(m, n, memo):
            if m < 0 or n < 0:
                return 0
            if m == 0 and n == 0:
                return 1
            if (m,n) not in memo:
                memo[(m,n)] = paths(m-1, n,memo) + paths(m, n-1,memo)
            return memo[(m,n)]

        return paths(m-1,n-1, {})


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def paths(matrix, m, n, memo):
            if m < 0 or n < 0 or matrix[m][n]==1:
                return 0
            if m == 0 and n == 0:
                return 1
            if (m,n) not in memo:
                memo[(m,n)] = paths(matrix,m-1, n,memo) + paths(matrix,m, n-1,memo)
            return memo[(m,n)]
        
        r = len(obstacleGrid)-1
        c = len(obstacleGrid[0])-1
        return paths(obstacleGrid,r, c, {})