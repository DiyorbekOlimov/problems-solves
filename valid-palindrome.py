# leetcode 125
from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        needed = ascii_lowercase + digits
        for c in s.lower():
            if c in needed: t += c
        return t == t[::-1]

s = Solution()
print(s.isPalindrome('0P'))