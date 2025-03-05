# ukol 1
def is_magic_square(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False
    s = sum(matrix[0])
    for row in matrix:
        if sum(row) != s:
            return False
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != s:
            return False
    if sum(matrix[i][i] for i in range(n)) != s:
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != s:
        return False
    return True

n = int(input("Velikost: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Řádek {i+1}: ").split()))
    matrix.append(row)
print(is_magic_square(matrix))

# ukol 2
def shift_list(lst, N):
    if not lst:
        return lst
    N = N % len(lst)
    return lst[-N:] + lst[:-N]

lst = list(map(int, input("Čísla: ").split()))
N = int(input("Posun: "))
print(shift_list(lst, N))

# ukol 3
def spiral_order(matrix):
    res = []
    if not matrix:
        return res
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for j in range(left, right+1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left-1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
    return res

n = int(input("Velikost: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Řádek {i+1}: ").split()))
    matrix.append(row)
print(spiral_order(matrix))

# ukol 4
def check_sudoku(board):
    for row in board:
        if sorted(row) != list(range(1, 10)):
            return False
    for j in range(9):
        if sorted(board[i][j] for i in range(9)) != list(range(1, 10)):
            return False
    for br in range(3):
        for bc in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[br*3+i][bc*3+j])
            if sorted(block) != list(range(1, 10)):
                return False
    return True

print("Sudoku:")
board = []
for i in range(9):
    row = list(map(int, input(f"Řádek {i+1}: ").split()))
    board.append(row)
print(check_sudoku(board))

# ukol 5
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

s = input("Výraz: ")
print(is_balanced(s))

# ukol 6
def generate_combinations(lst):
    def backtrack(start, current):
        print(current)
        for i in range(start, len(lst)):
            current.append(lst[i])
            backtrack(i+1, current)
            current.pop()
    backtrack(0, [])

lst = input("Prvky: ").split()
generate_combinations(lst)

# ukol 7
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

lst = list(map(int, input("Čísla: ").split()))
print(quick_sort(lst))

# ukol 8
def contains_all_alphabet(s):
    s = s.lower()
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s))

s = input("Text: ")
print(contains_all_alphabet(s))
