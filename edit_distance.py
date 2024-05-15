def rec_display_optimal_trace(array2d, w1, w2, i=0, j=0):
    # base case: tracing finishes, we are out of the matrix
    if i >= len(w1) or j >= len(w2):
        return
    # if same letters skips to diagonal cell
    if w1[i]==w2[j]:
        print('skip')
        return rec_display_optimal_trace(array2d, w1, w2, i + 1, j + 1)

    sols = (
        array2d[i+1][j + 1] + int(w1[i] != w2[j]),
        array2d[i+1][j] + 1,
        array2d[i][j+1] + 1
    )
    # save at which index is the minimum subsolution
    min_sol_index = sols.index(min(sols))
    # define the possible moves, then output the best one
    moves = (f'replace {w2[j]} by {w1[i]}', f'insert {w1[j]}', f'delete {w2[j]}')
    print(moves[min_sol_index])

    # move to the next cell, corresponding to the minimum subsolution
    i = i + int(min_sol_index != 2)
    j = j + int(min_sol_index != 1)
    # recursive call on the next cell
    rec_display_optimal_trace(array2d, w1, w2, i, j)


def edit_distance_rec(w1: str, w2: str, replace_is_double_cost: bool=False) -> int:
    # initiate the matrix filled by None, except for right and bottom borders
    dp = [[max(i, j) if i==0 or j==0 else None for j in range(len(w2),-1,-1)] for i in range(len(w1),-1,-1)]

    # this is the recursive edit distance method, it has access to dp, w1, w2
    def rec_ed(i, j) -> int:
        # if value is already solve, don't resolve it, just return the existing solution
        if dp[i][j] is not None:
            return dp[i][j]
        # find the possible subsolutions
        solutions = (
            rec_ed(i+1, j+1) + (1 + int(replace_is_double_cost)) * int(w1[i] != w2[j]),
            rec_ed(i+1, j) + 1,
            rec_ed(i, j+1) + 1
        )
        # save the minimum subsolution to the dp array
        dp[i][j] = min(solutions)
        # return the edit distance solution
        return dp[i][j]

    # call the recursive method with the starting case, indices 0,0
    distance = rec_ed(0,0)
    # display the steps to change w1 to w2 identified by the dp
    rec_display_optimal_trace(dp, w1, w2)
    return distance


def display_edit_table(array2d: list[list[int]], w1: str, w2: str) -> None:
    # display the edit distance 2d array as a table
    print('', *w2, sep='   ')
    for i, row in enumerate(array2d):
        if i < len(w1):
            print(w1[i], end=' ' * 2)
        else:
            print(end=' ' * 3)
        print(*row, sep=' | ')
        print(' ' * 3 + '_' * (4 * len(row) - 2))


def edit_distance(word1: str, word2: str, replace_is_double_cost: bool=False) -> int:
    """
    Args:
        - word1 (str)
        - word2 (str)
        - replace_is_double_cost (bool) specifies if replace is more expensive (2) than other operations (1)
    Returns:
        (int) minimum number of operations (delete, insert, replace) needed to change word1 to word2
    """
    # construct a 2d array, columns represent word2 letters, rows represent word1 letters
    # last row represents edits needed if word1 is empty, last col same for empty word2
    dp = [[max(i, j) for j in range(len(word2),-1,-1)] for i in range(len(word1),-1,-1)]

    # start filling the array from the bottom right corner; simplest case, then go up the hill
    for i in range(len(word1)-1, -1, -1):
        for j in range(len(word2)-1, -1, -1):
            # find edit_distance of the subproblem & add cost if needed
            dp[i][j] = min(
                dp[i+1][j+1] + (1 + int(replace_is_double_cost)) * int(word1[i] != word2[j]), # add cost for replacing letter if they are not same
                dp[i+1][j] + 1, # insert
                dp[i][j+1] + 1 # delete
            )

    display_edit_table(dp, word1, word2)
    return dp[0][0]


if __name__ == '__main__':
    a, b = [input(f'enter word {i + 1}: ') for i in range(2)]
    sol = edit_distance(a, b, True)
    print(f'\nminimum number of edits needed to change {a} to {b} is {sol}')
