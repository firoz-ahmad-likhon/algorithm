class Sort:
    def merge(self, ls1: list[int], ls2: list[int]) -> list[int]:
        stack = []
        
        while ls1 and ls2:
            if(ls1[0] < ls2[0]):
                stack.append(ls1.pop(0))
            else:
                stack.append(ls2.pop(0))
        stack += ls1
        stack += ls2
        
        return stack

cls = Sort()
print(cls.merge([1, 2, 3], [0]))
print(cls.merge([1, 2, 3], [2, 3, 4]))