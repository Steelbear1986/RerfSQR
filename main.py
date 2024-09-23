class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return ((num ** (1 / 2)) % 1 == 0)
