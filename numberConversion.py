class NumberConversion:
    def decimalToBinary(self, n: int) -> list[int]:
        remainder = []

        if (n == 0):
            return [n]

        while (n > 0):
            n, d = divmod(n, 2)
            remainder.append(d)

        return remainder[::-1]

    def BinaryToDecimal(self, n: int) -> int:
        num = i = 0

        while (n > 0):
            n, d = divmod(n, 10)
            num = d * (2 ** i) + num
            i += 1

        return num

cls = NumberConversion()
print(cls.decimalToBinary(123))
print(cls.decimalToBinary(0))
print(cls.decimalToBinary(28))

print(cls.BinaryToDecimal(1111011))
print(cls.BinaryToDecimal(0))
print(cls.BinaryToDecimal(11100))