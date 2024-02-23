class Array:
   def arrUpdate(self, arr: list[int], n: int, loc: int) -> list[int]:
           
       arr[loc] = n
       
       return  arr
        
cls = Array()
print(cls.arrUpdate([1, 2, 4], 3, 0))
print(cls.arrUpdate([1, 2, 4], 3, 1))
print(cls.arrUpdate([1, 2, 4], 3, 2))