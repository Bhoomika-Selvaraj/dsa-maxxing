def isPalindrome(s: str) -> bool:
    s = s.lower()
    ans = ""
    for i in s:
        if i.isalpha():
            ans += i
        elif i.isdigit():
            ans += i
    return ans == ans[::-1]


print(isPalindrome("0P"))

# Time complexity: O(n^2) in Python due to string concatenation
# Space complexity: O(n)

# Seems like two-pointer approach is better in terms of space complexity, let me try that toooooo...

# Two pointer approach


def isPalindrome2(s: str) -> bool:
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not (s[left].isalnum()):
            left += 1
        while left < right and not (s[right].isalnum()):
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# Time complexity: O(n)
# Space complexity: O(1)

# The time complexity is O(n) even with 3 while loops because each pointer (left and right)
# can move at most n steps total across all iterations. The inner while loops just skip
# non-alphanumeric characters, but we still process each character exactly once.
