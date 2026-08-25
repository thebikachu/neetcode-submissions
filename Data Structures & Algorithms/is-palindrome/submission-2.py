class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        

        s = ''.join(c for c in s if c.isalnum()).lower()
        # print(s.lower())
        p2 = len(s)-1

        while p2 > p1:
            if(s[p1] != s[p2]):
                return False
            
            p1 += 1
            p2 -= 1

        return True