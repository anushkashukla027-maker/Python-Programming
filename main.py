a = Array([5, 2, 9, 1, 7])

print("----- ARRAY OPERATIONS -----")
a.display()
a.find_sum()
a.find_max()
a.find_min()
a.search(9)
a.sort_array()

M1 = [[1, 2],
      [3, 4]]

M2 = [[5, 6],
      [7, 8]]

print("\n----- MATRIX CHECKS -----")
print("Valid Matrix:", a.is_valid_matrix(M1))
print("Can Add:", a.can_add_subtract(M1, M2))
print("Can Multiply:", a.can_multiply(M1, M2))
print("Is Square:", a.is_square(M1))
print("Is Symmetric:", a.is_symmetric(M1))

print("\n----- MATRIX OPERATIONS -----")
a.matrix_add(M1, M2)
a.matrix_subtract(M1, M2)
a.matrix_multiply(M1, M2)
a.matrix_transpose(M1)
a.matrix_range(M1)


V1 = [1, 2, 3]
V2 = [4, 5, 6]
a.dot_product(V1, V2)
a.cross_product(V1, V2)

print("\n--- Replace Diagonal of Matrix 1 ---")
a.replace_diagonal(M1)