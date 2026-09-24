class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            key = str(sorted(string))
            if key not in seen:
                seen[f"{key}"] = [string]
            else:
                seen[f"{key}"].append(string)
        return list(seen.values())