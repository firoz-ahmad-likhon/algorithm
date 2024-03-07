class Fibonacci:
    def __init__(self):
        self.memo = {}
    def recursiveFibonacci(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if (n <= 1):
            return n

        result = self.recursiveFibonacci(n - 1) + self.recursiveFibonacci(n - 2)

        self.memo[n] = result

        return result

n = 9
cls = Fibonacci()
print(cls.recursiveFibonacci(n))

for x in range(n + 1):
    print(cls.recursiveFibonacci(x), end=' ')
