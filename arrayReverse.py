class Array:
   def arrReverse(self, arr: list[int]) -> list[int]:
       length = len(arr)

       for x in range(length // 2):
           temp = arr[x]
           arr[x] = arr[length - 1]
           arr[length - 1] = temp
           length -= 1

       return arr

cls = Array()
print(cls.arrReverse([1, 2, 3]))
print(cls.arrReverse([3, 4, 5, 6]))
print(cls.arrReverse([10, 11, 12, 13, 14]))