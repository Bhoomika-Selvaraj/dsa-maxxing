def convert(s: str, numRows: int) -> str:

    if numRows == 1 or numRows >= len(s):
        return s

    current_row = 0
    down = True
    ans_arr = [""] * numRows
    for i in s:
        ans_arr[current_row] += i
        if down:
            current_row += 1
        else:
            current_row -= 1

        if current_row == numRows - 1:
            down = False
        if current_row == 0:
            down = True
    return "".join(ans_arr)


print(convert("helloworld", 4))


# Time complexity: O(n)
# Space complexity: O(n)

# Made me lose my mind
# I was thinking of a mathematical pattern to solve this but it was too complex, should have taken the simulation approach
