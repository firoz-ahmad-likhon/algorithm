class NumberAndDigits:
    def numberToDigits(self, n: int) -> list[int]:
        digits = []
        
        if(n == 0):
            return [n]
        
        while(n > 0):
            n, d = divmod(n, 10)
            digits.append(d)

        return digits[::-1]

    def digitsToNumber(self, n: list[int]) -> int:
        num = 0

        for i in range(len(n)):
            num = num * 10 + n[i]

        return num

cls = NumberAndDigits()
print(cls.numberToDigits(123))
print(cls.numberToDigits(0))
print(cls.numberToDigits(28))

print(cls.digitsToNumber([1, 2, 3]))
print(cls.digitsToNumber([0]))
print(cls.digitsToNumber([2, 8]))