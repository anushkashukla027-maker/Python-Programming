class Array:
    def _init_(self, arr):
        self.arr = arr

    def display(self):
        print("Array elements are:", self.arr)

    def find_sum(self):
        print("Sum of elements =", sum(self.arr))

    def find_max(self):
        print("Maximum element =", max(self.arr))

    def find_min(self):
        print("Minimum element =", min(self.arr))

    def search(self, key):
        print(key, "found in array" if key in self.arr else "not found in array")

    def sort_array(self):
        self.arr.sort()
        print("Sorted array:", self.arr)

    

    def matrix_add(self, A, B):
        result = [[A[i][j] + B[i][j] for j in range(len(A[0]))]
                  for i in range(len(A))]
        print("Matrix Addition Result:", result)

    def matrix_subtract(self, A, B):
        result = [[A[i][j] - B[i][j] for j in range(len(A[0]))]
                  for i in range(len(A))]
        print("Matrix Subtraction Result:", result)

    def matrix_multiply(self, A, B):
        result = [[sum(A[i][k] * B[k][j] for k in range(len(B)))
                  for j in range(len(B[0]))]
                  for i in range(len(A))]
        print("Matrix Multiplication Result:", result)

    def matrix_transpose(self, A):
        result = [[A[j][i] for j in range(len(A))]
                  for i in range(len(A[0]))]
        print("Matrix Transpose Result:", result)

 

    def dot_product(self, V1, V2):
        if len(V1) != len(V2):
            print("Dot product not possible!")
            return
        print("Dot Product =", sum(V1[i] * V2[i] for i in range(len(V1))))

    def cross_product(self, V1, V2):
        if len(V1) != 3 or len(V2) != 3:
            print("Cross product only for 3D vectors!")
            return
        cross = [
            V1[1] * V2[2] - V1[2] * V2[1],
            V1[2] * V2[0] - V1[0] * V2[2],
            V1[0] * V2[1] - V1[1] * V2[0]
        ]
        print("Cross Product =", cross)

    def matrix_range(self, A):
        flat = [val for row in A for val in row]
        print("Matrix Range (Max - Min) =", max(flat) - min(flat))