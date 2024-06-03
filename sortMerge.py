class Sort:
    def mergeSort(self, lst: list[int]) -> list[int]:
        if(len(lst) <= 1):
            return lst
        mid = len(lst) // 2
        l = lst[:mid]
        r = lst[mid:]
            
        return self.merge(self.mergeSort(l), self.mergeSort(r))
        
    def merge(self, ls1: list[int], ls2: list[int]) -> list:
        stack = []
        i = j = 0

        while i < len(ls1) and j < len(ls2):
            if (ls1[i] < ls2[j]):
                stack.append(ls1[i])
                i += 1
            else:
                stack.append(ls2[j])
                j += 1
        stack.extend(ls1[i:])
        stack.extend(ls2[j:])

        return stack

cls = Sort()
print(cls.mergeSort([12, 13, 11, 5, 4, 6, 7, 2]))
print(cls.mergeSort([1, 2, 3]))
print(cls.mergeSort([0]))
print(cls.mergeSort([]))