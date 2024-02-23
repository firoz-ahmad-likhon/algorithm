class Array:
   def arrDelete(self, arr: list[int], loc: int) -> list[int]:
       length = len(arr)

       for x in range(loc, length - 1):
           arr[x] = arr[x + 1]
       
       return  [arr[x] for x in range(length - 1)]
        
cls = Array()
print(cls.arrDelete([1, 2, 4], 0))
print(cls.arrDelete([1, 2, 4], 1))
print(cls.arrDelete([1, 2, 4], 2))