class Array:
   def arrInsert(self, arr: list[int], n: int, loc: int) -> list[int]:
       length = len(arr)
       arr.append(0)
       
       for x in range(length, loc, -1):
           arr[x] = arr[x - 1]
           
       arr[loc] = n
       
       return  arr
        
cls = Array()
print(cls.arrInsert([1, 2, 4], 3, 0))
print(cls.arrInsert([1, 2, 4], 3, 1))
print(cls.arrInsert([1, 2, 4], 3, 2))
print(cls.arrInsert([1, 2, 4], 3, 3))