class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in groups.key():
                groups[sorted_s].append(s)
            else:
                groups[sorted_s] = [s]
        
        return groups.values()
