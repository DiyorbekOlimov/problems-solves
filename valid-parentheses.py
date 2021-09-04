class Solution:
    def isValid(self, s: str) -> bool:
        for _ in range(len(s) // 2):
            for i in ('()', '[]', '{}'):
                s = s.replace(i, '')
        return s == ''

