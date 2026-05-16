class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(s)
        if n == 0:
            return True
        for i in range(n):
            if s[i]!=s[n-i-1]:
                return False
                break
        return True
