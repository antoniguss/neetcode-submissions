class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                ns += c
        s = ns

        l = len(s)
        for i in range(l//2):
            if s[i] != s[l - i - 1]:
                return False

        return True
        