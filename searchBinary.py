class Search:
    def binarySearch(self, lst: list, target) -> int:
        # Sort the list first
        lst.sort()

        low = 0
        high = len(lst) - 1

        while low <= high:
            mid = (low + high) // 2  # Calculate the middle index
            
            if lst[mid] == target:
                return mid  # Target found, return the index
            elif lst[mid] < target:
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half

        return -1  # Target not found, return -1

# Example usage:
cls = Search()
print(cls.binarySearch([12, 3, 5, 10, 8, 1], 1))  # Output: 0 (index of 1 in sorted list)
print(cls.binarySearch([3, 5, 7, 10, 9, 1], 7))   # Output: 3 (index of 7 in sorted list)
print(cls.binarySearch([7, 8, 9, 10, 1, 2], 3))   # Output: -1 (3 not found)
