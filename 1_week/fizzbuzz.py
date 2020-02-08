class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            if (i % 3) == 0 and (i % 5) == 0:
                result.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                result.append("Fizz")
                continue
            elif i % 5 == 0:
                result.append("Buzz")
                continue
            else:
                result.append(str(i))
        return result
