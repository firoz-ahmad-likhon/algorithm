class Sort:
    def insertionSort(self, lst: list) -> list[int]:
     
       for x in range(1, len(lst)):
           elem = lst[x]
           prev = x - 1
           
           while(prev >= 0 and lst[prev] > elem):
                   lst[prev + 1] = lst[prev]
                   prev -= 1
                   
           lst[prev + 1] = elem
           
       return lst

cls = Sort()
print(cls.insertionSort([12,3,5,10,8,1]))
print(cls.insertionSort([7,7,7,10,8,1]))
print(cls.insertionSort([17,7,13,9,0,1]))