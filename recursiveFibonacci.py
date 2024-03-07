class Fibonacci:
    def recursiveFibonacci(self, n: int) -> int:
        if(n <= 1):
            return n
       
        return self.recursiveFibonacci(n - 1) + self.recursiveFibonacci(n - 2)

n = 9
cls = Fibonacci()
print(cls.recursiveFibonacci(n))

for x in range(n + 1):
    print(cls.recursiveFibonacci(x), end = ' ')