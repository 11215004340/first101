#CLIMBING STAIR

class Solution(object):
    def climbStairs(self, n):
        memo = {} # Initialize an empty dictionary to store computed results

        return self.ways(n, memo) # Call the ways method with n and memo as arguments and return the result
    
    def ways(self, n, memo):

# Define a helper method named ways which takes n and memo as input

        if n in memo: # Check if the result for n is already computed and stored in memo
            return memo[n] # Return the stored result directly
        
# Base cases: if n is 1 or 2, return 1 or 2 respectively
        if n == 1:
            return 1
        elif n == 2:
            return 2

# Recursive case: calculate the result for n by summing up results for n-1 and n-2

        memo[n] = self.ways(n - 1, memo) + self.ways(n - 2, memo)
        return memo[n] # Store the calculated result in memo and return it
