class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_1 = {}
        counter_2 = {}
        if set(s) != set(t):
            return False

        for letter in s:
            if letter in counter_1.keys():
                counter_1[letter] += 1
            else:
                counter_1[letter] = 1
        
        for letter in t:
            if letter in counter_2.keys():
                counter_2[letter] += 1
            else:
                counter_2[letter] = 1
        
        if counter_1 == counter_2:
            return True
        return False