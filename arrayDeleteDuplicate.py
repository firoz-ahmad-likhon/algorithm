class Array:
    def arrDeleteDuplicate(self, arr: list[int]) -> list[int]:
        arr.sort()
        l = len(arr)
        i = 0

        while (i < l - 1):
            if (arr[i] == arr[i + 1]):
                arr.pop(i + 1)
                l -= 1
                i -= 1
            i += 1

        return arr

    def arrDeleteDuplicateInPlace(self, arr: list[int]) -> list[int]:
        arr.sort()
        l = len(arr)
        unique = 1

        for i in range(l - 1):
            if arr[i] != arr[i + 1]:
                arr[unique] = arr[i + 1]
                unique += 1

        return arr if l == 0 else [arr[i] for i in range(unique)]

    def arrDeleteDuplicateBySet(self, arr: list[int]) -> list[int]:

        return list(set(arr))

    def arrDeleteDuplicateBySetOrder(self, arr: list[int]) -> list[int]:
        seen = set()
        result = []

        for i in arr:
            if i not in seen:
                seen.add(i)
                result.append(i)

        return result


cls = Array()
print(cls.arrDeleteDuplicate([1, 7, 6, 5, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7]))
print(cls.arrDeleteDuplicate([1, 4, 5, 6, 6, 8, 9]))
print(cls.arrDeleteDuplicate([1, 1]))
print(cls.arrDeleteDuplicate([1]))
print(cls.arrDeleteDuplicate([]))

print(cls.arrDeleteDuplicateInPlace([1, 7, 6, 5, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7]))
print(cls.arrDeleteDuplicateInPlace([1, 4, 5, 6, 6, 8, 9]))
print(cls.arrDeleteDuplicateInPlace([1, 1]))
print(cls.arrDeleteDuplicateInPlace([1]))
print(cls.arrDeleteDuplicateInPlace([]))

print(cls.arrDeleteDuplicateBySetOrder([1, 7, 6, 5, 2, 2, 3, 4, 5, 6, 6, 7, 7, 7]))
print(cls.arrDeleteDuplicateInPlace([1, 4, 5, 6, 6, 8, 9]))
print(cls.arrDeleteDuplicateInPlace([1, 1]))
print(cls.arrDeleteDuplicateInPlace([1]))
print(cls.arrDeleteDuplicateInPlace([]))
