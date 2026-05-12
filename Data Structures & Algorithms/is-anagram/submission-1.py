class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        contains = {}
        for letter in s:
            contains[letter] = contains.get(letter, 0) + 1
        
        for letter in t:
            contains[letter] = contains.get(letter, 0) - 1
            if contains[letter] < 0:
                return False
        
        return True
        