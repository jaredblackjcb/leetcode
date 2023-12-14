from collections import defaultdict
from typing import List


# 2.1 Find all indices in s where i is a starting location of an anagram of w
def findAnagramIndices(w: str, s: str) -> List[int]:
    ans = []
    def createMap(s):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        print(d)
        return d

    # Create a map to represent the word to compare
    w_dict = createMap(w)

    # Start at the index of the length of w - 1 and step backwards
    start, end = 0, len(w) - 1
    while end <= len(s) - 1:
        # If the char at that index is not in w_dict, reset start position to i + 1
        if s[end] in w_dict:
            # Create a mapping for the slice and compare it to w_dict. If at any point s_dict[c] > w_dict[c], new starting point is i
            # for c in reversed(s[start: end+1]):
            s_dict = createMap(s[start:end+1])
            print(f"s_dict: {s_dict}")
            if s_dict == w_dict:
                ans.append(start)
            start += 1
            end += 1
        else:
            start = end + 1
            end = start + len(w) - 1

    return ans

# Could be better to create dict of word and initial window, then add start index to answer every time they match.
# I would need to increment and decrement counters each time I moved an index, and make sure to delete the key for
# any 0 values from the dict any time I decrement

# 2.2 Palindrome Pairs
def palindromePairs(arr: List[str]) -> List[tuple]:
    ans = []
    # Create a dictionary where the keys are the words in the arr and values are the index of the word
    d = {}
    for i, w in enumerate(arr):
        # Assume all words are unique for now
        d[w] = i

    for i, prefix in enumerate(arr):
        # Reverse each word
        backward = prefix[::-1]
        if prefix != backward:
            # Check whether the original word plus the reversed segment is a palindrome
            for j in range(len(backward)):
                # Increment start value of slice on each iteration
                suffix = backward[j:]
                # Generate word to check
                word = prefix + suffix
                # If suffix is in dict and word is a palindrome, add the indices tuple to the answer
                if suffix in d and isPalindrome(word):
                    ans.append((i, d[suffix]))
    return ans

def isPalindrome(w):
    start, end = 0, len(w) - 1
    while start < end:
        if w[start] != w[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    print(palindromePairs(["code", "edoc", "da", "d"]))
