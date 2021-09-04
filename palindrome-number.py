class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x1 = x
        y = 0
        while x1 > 0:
            y = y*10 + x1%10
            x1 = x1 // 10
        return x == y
