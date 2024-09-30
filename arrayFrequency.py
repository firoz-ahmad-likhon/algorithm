class array:
    def frequency(self, arr: list[int]) -> dict[int, int]:
        counter = {}

        for i in range(len(arr)):
            if arr[i] in counter:
                counter[arr[i]] += 1
            else:
                counter[arr[i]] = 1

        return counter

cls = array()
print(cls.frequency([2, 1, 1, 2, 3, 4, 4, 4, 4]))