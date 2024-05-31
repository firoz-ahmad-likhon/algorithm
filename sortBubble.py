class Sort:
    def bubbleSort(self, lst: list) -> list[int]:
        
        length = len(lst)
        for x in range(length - 1):   
            for y in range(length - 1 - x):
                if(lst[y] > lst[y + 1]):
                    lst[y], lst[y + 1] = lst[y + 1], lst[y]
           
        return lst

cls = Sort()
print(cls.bubbleSort([12,3,5,10,8,1]))
print(cls.bubbleSort([7,7,7,10,8,1]))
print(cls.bubbleSort([17,7,13,9,0,1]))

