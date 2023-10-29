from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        strs_table = {}
    
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in strs_table:
                strs_table[sorted_string] = [] 
            strs_table[sorted_string].append(string)
        return list(strs_table.values())
    
    
    def groupAnagrams2(self, strs):
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] +=1
            res[tuple(count)].append(str)

        return res.values()

solution = Solution()

print(solution.groupAnagrams2(strs = ["eat","tea","tan","ate","nat","bat"]))