from copy import deepcopy


def diagonals(i: int, j: int):
    """
    Takes a pair of coordinates and returns a list of coordinates that are diagonal to it.

    :param i: row
    :param j: column
    :return: list of tuples
    """
    return [(n, m) for n in range(8) for m in range(8) if i - j == n - m or i - n == m - j]


def safe(board: list, i: int, j: int):
    return not (any(board[i]) or any([row[j] for row in board]) or any([board[k][l] for k, l in diagonals(i, j)]))


def update(board: list, i: int, j: int):
    temp = deepcopy(board)
    temp[i][j] = 1
    return temp


def solution(n: int):
    if n == 1:
        empty_board = [[0 for _ in range(8)] for _ in range(8)]
        return [update(empty_board, i, 0) for i in range(8)]

    """lst = list()
    for board in solution(n - 1):
        for i in range(8):
            if safe(board, i, n - 1):
                lst.append(update(board, i, n-1))
    return lst"""
    return [update(board, i, n-1) for board in solution(n - 1) for i in range(8) if safe(board, i, n - 1)]


print(len(solution(8)))
