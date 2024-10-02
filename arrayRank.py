class Array:
    def rank(self, arr: list[int]) -> list[int]:
        if not arr:  # Check if the array is empty
            return []

        # Create a sorted list of unique elements and create a rank mapping
        rnk = {val: rank for rank, val in enumerate(sorted(set(arr)), start=1)}

        # Return ranks corresponding to the original array
        return [rnk[val] for val in arr]

# Example usage
cls = Array()
print(cls.rank([100, 200, 100, 300, 150]))  # Output: [2, 4, 2, 5, 3]
print(cls.rank([2, 3, 2, 4, 1, 3, 5, 5, 7]))  # Output: [2, 3, 2, 4, 1, 3, 5, 5, 6]
print(cls.rank([40,10,20,30]))  # Output: [4, 1, 2, 3]
