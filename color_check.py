"""Checks by color"""


from typing import List


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
        f = 0
        while k < 5:
            el = board[i+k][j+f]
            if el.isnumeric():
                if el not in check_lst:
                    check_lst.append(el)
                else:
                    return False
            k += 1
        k -= 1
        while f < 5:
            el = board[i+k][j+f]
            if el.isnumeric():
                if el not in check_lst:
                    check_lst.append(el)
                else:
                    return False
            f += 1
        count += 1
        check_lst.clear()
        i -= 1
        j += 1
    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
