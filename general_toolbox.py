class ToolBox:
    # Check if string in given index is a palindrome
    def isPalindrome(self, i, j, s):
        j -= 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    # Check if string is palindrome
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
    # Find the longest substring that meets x criteria
    def longestSubstringX(self, s):
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if self.isPalindrome(start, start + length, s):
                    return s[start:start+length]




