class Solution(object):
    def climeStairs (self, n): 
        memo = {}
        return self.ways(n, memo)
    def ways(self, n , memo):
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        memo[n] = self.ways(n - 1, memo) + self.ways(n - 2, memo)
        return memo[n]
    