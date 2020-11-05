class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def insert(self):
        new_matrix = []
        print("Enter matrix: ")
        for j in range(0, self.rows):
            new_matrix.append([float(j) for j in input().split()])
        return new_matrix


def matrix_size():
    rows, columns = input("Enter size of matrix: ").split()
    return int(rows), int(columns)


def print_result(matrix):
    print("The result is:")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    print("")


# ADD MATRIX
def add_matrix(matrix1, matrix2):

    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        new_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in
                      range(len(matrix1))]

        print_result(new_matrix)
    else:
        print("ERROR")

    menu()


# MULTIPLY BY CONST
def multiply_by_const(matrix):

    CONST = int(input("Enter constant: "))
    new_matrix = [[matrix[i][j] * CONST for j in range(len(matrix[0]))] for i in
                  range(len(matrix))]

    print_result(new_matrix)

    menu()


# MULTIPLY BY MATRIX
def multiply_by_matrix(matrix1, matrix2):
    if len(matrix1) == len(matrix2[0]):
        result = [[0 for j in range(len(matrix2[0]))] for i in
                      range(len(matrix1))]
        for i in range(len(matrix1)):
            # iterate through columns of Y
            for j in range(len(matrix2[0])):
                # iterate through rows of Y
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        print_result(result)

    else:
        print("ERROR")

    menu()


# TRANSPOSE MATRIX
def transpose_matrix():
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    command = int(input("Your choice: "))
    if command == 1:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        main_diag_trans(matrix1_list)
        menu()
    elif command == 2:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        side_diag_trans(matrix1_list)
        menu()
    elif command == 3:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        vertical_trans(matrix1_list)
        menu()
    elif command == 4:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        horizontal_trans(matrix1_list)
        menu()


def main_diag_trans(matrix):
    new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print_result(new_matrix)


def side_diag_trans(matrix):
    new_matrix = [[matrix[len(matrix[0]) - j - 1][len(matrix) - i - 1] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print_result(new_matrix)


def vertical_trans(matrix):
    new_matrix = [[matrix[i][len(matrix) - j - 1] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    print_result(new_matrix)


def horizontal_trans(matrix):
    new_matrix = [[matrix[len(matrix[0]) - i - 1][j] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print_result(new_matrix)


# DETERMINANT MATRIX
def matrix_minor(m,i,j):
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
            det += ((-1)**i)*matrix[0][i]*determinant_matrix(matrix_minor(matrix,0,i))
        return det


# INVERSE MATRIX
def inverse_matrix(matrix):
    first_det = determinant_matrix(matrix)

    if first_det == 0:
        print("This matrix doesn't have an inverse.")
        menu()
    else:
        cofactors = []
        for r in range(len(matrix)):
            cofactor_row = []
            for c in range(len(matrix)):
                minor = matrix_minor(matrix, r, c)
                cofactor_row.append(((-1) ** (r + c)) * determinant_matrix(minor))
            cofactors.append(cofactor_row)
        new_matrix = [[cofactors[j][i] for j in range(len(cofactors))] for i in range(len(cofactors[0]))]
        for r in range(len(new_matrix)):
            for c in range(len(new_matrix)):
                new_matrix[r][c] = new_matrix[r][c] / first_det

        print_result(new_matrix)


def menu():
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    command = int(input("Your choice: "))
    if command == 1:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        second_rows, second_columns = matrix_size()
        matrix2 = Matrix(second_rows, second_columns)
        matrix2_list = matrix2.insert()
        add_matrix(matrix1_list, matrix2_list)
    elif command == 2:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        multiply_by_const(matrix1_list)
    elif command == 3:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        second_rows, second_columns = matrix_size()
        matrix2 = Matrix(second_rows, second_columns)
        matrix2_list = matrix2.insert()
        multiply_by_matrix(matrix1_list, matrix2_list)
    elif command == 4:
        transpose_matrix()
    elif command == 5:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        print(determinant_matrix(matrix1_list))
        menu()
    elif command == 6:
        first_rows, first_columns = matrix_size()
        matrix1 = Matrix(first_rows, first_columns)
        matrix1_list = matrix1.insert()
        inverse_matrix(matrix1_list)
        menu()
    elif command == 0:
        exit()


menu()

