"""Puzzle game"""

from typing import List

def columns_check(board):
    '''
    >>> columns_check(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    >>> columns_check(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 ",\
        " 6  83  *","3   9  **","  8  2***","  2  ****"])
    True
    '''
    list_rows = [list(row) for row in board]
    t_matrix = map(list, zip(*list_rows))
    transpose_matrix = [''.join(row) for row in t_matrix]
    all_columns = []
    for line in transpose_matrix:
        column = []
        for j in line:
            if j.isdigit():
                column.append(int(j))

        all_columns.append(column)

    return all(len(set(_x)) == len(_x) for _x in all_columns)


def check_row(board):
    """
    This function check all elements in row is unique
    """
    flag = True
    for i in board:
        for j in i:
            if j in ('*', ' ') and i.count(j) > 1:
                flag = False
                break
    return flag


def color_check(board: List[str]) -> bool:
    """
    Check by color
    Args:
        board (List):  board to check
    Returns:
        bool: result of checking
    >>> color_check(["**** ****",\
"***15****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    >>> color_check(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    True
    >>> color_check(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"  1  9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"  2  ****"])
    False
    """
    check_lst = []
    i = 4
    j = 0
    count = 0
    while count < 5:
        k = 0
        ind = 0
        while k < 5:
            elem = board[i+k][j+ind]
            if elem.isnumeric():
                if elem not in check_lst:
                    check_lst.append(elem)
                else:
                    return False
            k += 1
        k -= 1
        ind = 1
        while ind < 5:
            elem = board[i+k][j+ind]
            if elem.isnumeric():
                if elem not in check_lst:
                    check_lst.append(elem)
                else:
                    return False
            ind += 1
        count += 1
        check_lst.clear()
        i -= 1
        j += 1
    return True

def validate_board(board: List[str]) -> bool:
    """
    final check
    Args:
        board (List[str])
    Returns:
        bool: result
    """
    if columns_check(board) and color_check(board) and check_row(board):
        return True
    return False
