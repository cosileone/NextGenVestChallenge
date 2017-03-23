import operator
import numpy

sample_matrix = [[1, 2, 3, 4, 5],
                 [1, 1, 2, 3, 5],
                 [3, 4, 5, 5, 5],
                 [3, 4, 5, 9, 5],
                 [1, 1, 5, 5, 25]]


def find_max_scholarship(matrix, scholarship_limit=11):
    best_horizontal = max_horizontal(matrix, scholarship_limit)
    best_vertical = max_vertical(matrix, scholarship_limit)
    best_diag_down = max_diagonal_down(matrix, scholarship_limit)
    best_diag_up = max_diagonal_up(matrix, scholarship_limit)

    return find_max_sequence([best_horizontal, best_vertical, best_diag_down, best_diag_up])


def find_max_sequence(sequence_list):
    curr_max = 0
    result = []

    for row in sequence_list:
        total = reduce(operator.mul, row)
        if total > curr_max:
            curr_max = total
            result = row

    return result


def make_subsequences(numlist, limit):
    index = 0
    list_size = len(numlist)
    matrix = []

    if limit > list_size:
        matrix.append(numlist)
    else:
        while index + limit <= list_size:
            sublist = numlist[index:index + limit]
            matrix.append(sublist)
            index += 1

    return matrix


def max_horizontal(matrix, limit):
    if limit < len(matrix):
        return find_max_sequence([find_max_sequence(make_subsequences(x, limit)) for x in matrix])
    else:
        return find_max_sequence(matrix)


def max_vertical(matrix, limit):
    matrix = numpy.transpose(matrix)  # transpose matrix to turn columns into rows

    if limit:
        return find_max_sequence([find_max_sequence(make_subsequences(x, limit)) for x in matrix])
    else:
        return find_max_sequence(matrix)


def max_diagonal_up(matrix, limit):
    # first we convert matrix to numpy arrays
    new_matrix = numpy.array(matrix)

    # then we find the diagonals and put them into a list
    diags = [new_matrix[::-1, :].diagonal(i) for i in range(-new_matrix.shape[0] + 1, new_matrix.shape[1])]

    # then we convert elements back to lists
    diags = [elem.tolist() for elem in diags]

    if limit < max([len(x) for x in diags]):
        return find_max_sequence([find_max_sequence(make_subsequences(x, limit)) for x in diags])
    else:
        return find_max_sequence(matrix)


def max_diagonal_down(matrix, limit):
    # first we convert matrix to numpy arrays
    new_matrix = numpy.array(matrix)

    # then we find the diagonals and put them into a list
    diags = [new_matrix.diagonal(i) for i in range(new_matrix.shape[1] - 1, -new_matrix.shape[0], -1)]

    # then we convert elements back to lists
    diags = [elem.tolist() for elem in diags]

    if limit < max([len(x) for x in diags]):
        return find_max_sequence([find_max_sequence(make_subsequences(x, limit)) for x in diags])
    else:
        return find_max_sequence(matrix)


print find_max_scholarship(sample_matrix, 3)
