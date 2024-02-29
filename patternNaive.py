class Pattern:
    def patternNaive(self, haystack: str, needle: str) -> int:

        length = len(haystack)
        needle_length = len(needle)
        for i in range(length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1

cls = Pattern()
print(cls.patternNaive("xyz abc def abc def abcdef", 'abc'))
print(cls.patternNaive("xyz abc def abc def", 'def'))
print(cls.patternNaive("xyz abc def abc defxyz", 'xyz'))