matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]

def diagonal(matrix):
	diagonal1 = 0
	diagonal2 = 0
	for i in range(len(matrix)):
		diagonal1 += matrix[i][i]
		diagonal2 += matrix[i][len(matrix)-i-1]
	return diagonal1 - diagonal2

print(diagonal(matrix))