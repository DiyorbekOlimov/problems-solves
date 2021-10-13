# leetcode 69

class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i < x:
            if (i+1)**2 > x: break
            i += 1
        return i
