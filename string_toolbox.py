class StringToolbox:
    # Helper method to reverse all characters in a string
    @staticmethod
    def reverseChars(s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1
        # Switch start and end indexes in place
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)