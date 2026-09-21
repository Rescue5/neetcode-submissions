class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        p1 = 0
        p2 = length - 1
        s = s.lower()
        while p2>=p1:
            while not s[p1].isalnum() and p1 < p2:
                p1+=1
            while not s[p2].isalnum() and p1 < p2:
                p2-=1

            if s[p1] != s[p2]:
                return False
            
            p1+=1
            p2-=1

        return True