#CLIMBING STAIR

class Solution(object):
    def climbStairs(self, n): 
        memo = {} #Initializeanemptydictionarytostorecomputed results 
        return self.ways(n, memo) #Callthewaysmethodwithnand memoasargumentsandreturntheresult 
    
    def ways(self, n, memo): #Defineahelpermethodnamedwayswhichtakesnandmemoas input 
        if n in memo: #Checkiftheresultfornisalreadycomputed andstoredinmemo 
            return memo[n] #Returnthestoredresultdirectly 
        
        #Basecases:ifnis1or2,return1or2respectively 
        if n == 1: 
            return 1 
        elif n == 2: 
            return 2 #Recursivecase:calculatetheresultfornbysummingup resultsforn-1andn-2 
            
        memo[n] = self.ways(n - 1, memo) + self.ways(n-2, memo) 
        return memo[n] #Storethecalculatedresultinmemoandreturn it