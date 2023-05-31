scalar = 3
vector = [1,2,4,5,-1]
vector_1 = [-199 , 2, 3,6,7]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[1][0]
scalar_mult_vector = []
vector_add_vector = []

for i in vector:
    scalar_mult_vector.append(scalar * i)

for i in range(len(vector)):
    vector_add_vector.append(vector[i] + vector_1[i])

print(scalar_mult_vector)
print(vector_add_vector)