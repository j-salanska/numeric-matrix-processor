def insert_first():
    first_rows, first_columns = input("Enter size of first matrix: ").split()
    first_rows = int(first_rows)
    first_columns = int(first_columns)
    first_matrix = []
    print("Enter first matrix: ")
    for j in range(0, first_rows):
        first_matrix.append([float(j) for j in input().split()])
    return first_rows, first_columns, first_matrix


def insert_second():
    second_rows, second_columns = input("Enter size of second matrix: ").split()
    second_rows = int(second_rows)
    second_columns = int(second_columns)
    second_matrix = []
    print("Enter second matrix: ")
    for x in range(0, second_rows):
        second_matrix.append([float(x) for x in input().split()])
    return second_rows, second_columns, second_matrix


# ADD MATRIX
def add_matrix():
    first_rows, first_columns, first_matrix = insert_first()
    second_rows, second_columns, second_matrix = insert_second()

    if first_rows == second_rows and first_columns == second_columns:
        new_matrix = [[first_matrix[i][j] + second_matrix[i][j] for j in range(len(first_matrix[0]))] for i in
                      range(len(first_matrix))]

        print("The result is:")
        for i in range(first_rows):
            for j in range(first_columns):
                print(new_matrix[i][j], end=" ")
            print()
        print("")
    else:
        print("ERROR")


# MULTIPLY BY CONST
def multiply_by_const():
    first_rows, first_columns, first_matrix = insert_first()

    CONST = int(input("Enter constant: "))
    new_matrix = [[first_matrix[i][j] * CONST for j in range(len(first_matrix[0]))] for i in
                  range(len(first_matrix))]

    print("The result is:")
    for i in range(first_rows):
        for j in range(first_columns):
            print(new_matrix[i][j], end=" ")
        print()
    print("")


# MULTIPLY BY MATRIX
def multiply_by_matrix():
    first_rows, first_columns, first_matrix = insert_first()
    second_rows, second_columns, second_matrix = insert_second()
    if first_columns == second_rows:
        result = [[0 for j in range(len(second_matrix[0]))] for i in
                      range(len(first_matrix))]
        for i in range(len(first_matrix)):
            # iterate through columns of Y
            for j in range(len(second_matrix[0])):
                # iterate through rows of Y
                for k in range(len(second_matrix)):
                    result[i][j] += first_matrix[i][k] * second_matrix[k][j]

        print("The result is:")
        for i in range(first_rows):
            for j in range(second_columns):
                print(result[i][j], end=" ")
            print()
        print("")

    else:
        print("ERROR")


def main_diag_trans():
    first_rows, first_columns, first_matrix = insert_first()
    new_matrix = [[first_matrix[j][i] for j in range(len(first_matrix))] for i in range(len(first_matrix[0]))]

    print("The result is:")
    for i in range(first_rows):
        for j in range(first_columns):
            print(new_matrix[i][j], end=" ")
        print()
    print("")


def side_diag_trans():
    first_rows, first_columns, first_matrix = insert_first()
    new_matrix = [[first_matrix[len(first_matrix[0]) - j - 1][len(first_matrix) - i - 1] for j in range(len(first_matrix))] for i in range(len(first_matrix[0]))]


    print("The result is:")
    for i in range(first_rows):
        for j in range(first_columns):
            print(new_matrix[i][j], end=" ")
        print()
    print("")


def vertical_trans():
    first_rows, first_columns, first_matrix = insert_first()
    new_matrix = [[first_matrix[i][len(first_matrix) - j - 1] for j in range(len(first_matrix[0]))] for i in range(len(first_matrix))]


    print("The result is:")
    for i in range(first_rows):
        for j in range(first_columns):
            print(new_matrix[i][j], end=" ")
        print()
    print("")


def horizontal_trans():
    first_rows, first_columns, first_matrix = insert_first()
    new_matrix = [[first_matrix[len(first_matrix[0]) - i - 1][j] for j in range(len(first_matrix))] for i in range(len(first_matrix[0]))]

    print("The result is:")
    for i in range(first_rows):
        for j in range(first_columns):
            print(new_matrix[i][j], end=" ")
        print()
    print("")


# TRANSPOSE MATRIX
def transpose_matrix():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    command = int(input("Your choice: "))
    if command == 1:
        main_diag_trans()
        menu()
    elif command == 2:
        side_diag_trans()
        menu()
    elif command == 3:
        vertical_trans()
        menu()
    elif command == 4:
        horizontal_trans()
        menu()


# DETERMINANT MATRIX
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def determinant_matrix(matrix):
    det = 0
    if len(matrix) == 1 and len(matrix[0]) == 1:
        det = matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        det = matrix[0][0] * matrix[1][1] - (matrix[0][1] * matrix[1][0])
        return det
    else:
        for i in range(len(matrix)):
            det += ((-1)**i)*matrix[0][i]*determinant_matrix(getMatrixMinor(matrix,0,i))
        return det


# INVERSE MATRIX
def inverse_matrix():
    first_rows, first_columns, first_matrix = insert_first()
    first_det = determinant_matrix(first_matrix)

    if first_det == 0:
        print("This matrix doesn't have an inverse.")
        menu()
    else:
        cofactors = []
        for r in range(len(first_matrix)):
            cofactor_row = []
            for c in range(len(first_matrix)):
                minor = getMatrixMinor(first_matrix, r, c)
                cofactor_row.append(((-1) ** (r + c)) * determinant_matrix(minor))
            cofactors.append(cofactor_row)
        new_matrix = [[cofactors[j][i] for j in range(len(cofactors))] for i in range(len(cofactors[0]))]
        for r in range(len(new_matrix)):
            for c in range(len(new_matrix)):
                new_matrix[r][c] = new_matrix[r][c] / first_det

        print("The result is:")
        for i in range(len(new_matrix[0])):
            for j in range(len(new_matrix)):
                print(new_matrix[i][j], end=" ")
            print()
        print("")
        return new_matrix


def menu():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    command = int(input("Your choice: "))
    if command == 1:
        add_matrix()
        menu()
    elif command == 2:
        multiply_by_const()
        menu()
    elif command == 3:
        multiply_by_matrix()
        menu()
    elif command == 4:
        transpose_matrix()
        menu()
    elif command == 5:
        first_rows, first_columns, first_matrix = insert_first()
        print(determinant_matrix(first_matrix))
        menu()
    elif command == 6:
        inverse_matrix()
        menu()
    elif command == 0:
        exit()


menu()

