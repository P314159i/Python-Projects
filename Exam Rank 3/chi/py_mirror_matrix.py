#! /usr/bin/env Python3

def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for x in matrix:
        x.reverse()
    return matrix


if __name__ == "__main__":
    print(f"[[3,2,1],[6,5,4]] -> {mirror_matrix([[1,2,3],[4,5,6]])}")