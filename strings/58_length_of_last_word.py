def lengthOfLastWord(s: str) -> int:
    s = s.strip()
    left = len(s) - 1
    while s[left] != " " and left >= 0:
        left -= 1
    return len(s[left + 1 : len(s)])


print(lengthOfLastWord("Hello World"))

# Time complexity: O(n)
# Space complexity: O(n) because strip creates a new string
