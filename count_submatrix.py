
class Main:
    def count_submatrix(self, A, B):
        count = 0

        if len(B) > len(A) or len(B[0]) > len(A[0]):
            return "Can't be found"

        arr = sum(B, [])

        for row in A:
            for element in row:
                for value in arr:
                    if value in row:
                        count += 1
                        self.remove_matrix_element(A, value)
        if count == len(B) * len(B[0]):
            return f"The submatrix can be found in the matriz {count // (len(B) * len(B[0]))} time(s)"
        else:
            return "Can't be found"
        
    def remove_matrix_element(self, matrix, element):
        for row in matrix:
            if element in row:
                row.remove(element)

A = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

B = [
        [8, 9],
        [13, 14]
    ]

main = Main()
result = main.count_submatrix(A, B)
print(result)