def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:

    i = 0
    for x in matrix:
        x = x[::-1]
        matrix[i] = x
        i += 1    
    return matrix

if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))
