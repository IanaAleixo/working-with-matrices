
class Main:
    def invert_columns(matrix):
        n = len(matrix)

        if n == 1:
            return matrix
        
        main_diagonol = []
        secondary_diagonal = []
        for i in range(len(matrix)):
            main_diagonol.append(matrix[i][i])
            secondary_diagonal.append(matrix[i][n-1])
            n = n -1

        for i in range(len(matrix)):
            matrix[i][i] = main_diagonol[n-1]
            matrix[i][n-1] = secondary_diagonal[n-1]
            n = n -1
    
        return matrix

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    invert_columns(matrix)
    print(matrix)