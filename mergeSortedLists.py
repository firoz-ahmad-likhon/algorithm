class Sort:
    def merge(self, ls1: list[int], ls2: list[int]) -> list[int]:
        stack = []
        i = j = 0
        
        while i < len(ls1) and j < len(ls2):
            if(ls1[i] < ls2[j]):
                stack.append(ls1[i])
                i += 1
            else:
                stack.append(ls2[j])
                j += 1
        stack.extend(ls1[i:])
        stack.extend(ls2[j:])
        
        return stack

cls = Sort()
print(cls.merge([1, 2, 3], [0]))
print(cls.merge([1, 2, 3], [2, 3, 4]))