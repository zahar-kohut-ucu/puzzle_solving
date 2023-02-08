def check_row(board):
    """
    This function check all elements in row is unique
    """
    flag = True
    for i in board:
        for w in i:
            if w != '*' and w != ' ' and i.count(w) > 1:
                flag = False
                break
    return flag
