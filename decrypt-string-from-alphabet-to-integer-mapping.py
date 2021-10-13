# leetcode 1309
from string import ascii_lowercase as lc


class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i, c in enumerate(lc[9:], 10): s = s.replace(f'{i}#', c)
        for i, c in enumerate(lc[:9], 1): s = s.replace(f'{i}', c)
        return s
