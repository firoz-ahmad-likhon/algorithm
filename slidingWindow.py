class SlidingWindow:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    def maxSum(self):
        n = len(self.arr)
        max = sum = 0

        for i in range(self.k):
            sum += self.arr[i]
        max = sum

        for i in range(n - self.k):
            sum = sum - self.arr[i] + self.arr[i + self.k]
            if sum > max:
                max = sum

        return max


print(SlidingWindow([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3).maxSum())
print(SlidingWindow([1, 4, 2, 10, 2, 3, 1, 0, 20], 4).maxSum())
