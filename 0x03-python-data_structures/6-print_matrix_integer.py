#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            y = 0
            for m in i:
                if y < len(i) - 1:
                    print("{:d}".format(m), end=" ")
                else:
                    print("{:d}".format(m))
                    break
                y += 1
    else:
        print("")
