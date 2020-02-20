class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            calculation = self.myPow(x, n/2)
            return calculation * calculation
        elif n > 0:
            return x * self.myPow(x, n-1)
        else:
            return 1.0 / x * self.myPow(x, n+1)
