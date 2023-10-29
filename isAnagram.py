class Solution(object):
    def isAnagram(self, s, t):
        anaHash = {}
        
        for l in s:
            if l in anaHash:
               anaHash[l] = anaHash.get(l) + 1
            else:   
                anaHash[l] = 1
        
        for l in t:
            if l in anaHash:
               anaHash[l] = anaHash.get(l) - 1 
            else:
               anaHash[l] = 1
            if anaHash.get(l) == 0:
                anaHash.pop(l)
            
        if len(anaHash) == 0:
            return True
        else:
            return False
        

solution = Solution()

print(solution.isAnagram(s = "a", t = "ab"))
