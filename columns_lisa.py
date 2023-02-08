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
