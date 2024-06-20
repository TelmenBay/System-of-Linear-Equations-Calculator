import numpy as np
import pandas as pd

def input_matrix():
    # Ask for the number of equations (rows)
    n = int(input("Enter the number of equations: "))
    matrix = []

    # Loop to get each row of the matrix
    for i in range(n):
        row = input(f"Enter coefficients of equation {i+1} separated by spaces: ").split()
        row = [float(num) for num in row]
        matrix.append(row)
    
    return pd.DataFrame(np.array(matrix))
    
def div(matrix, i):
    d = matrix.iloc[i, i]
    for j in range(len(matrix.columns)):
        matrix.iloc[i, j] = matrix.iloc[i, j] / d
    return matrix  
    
def UpperTriangular(matrix):
    n = len(matrix.index)
    for i in range(n):
        # Make the diagonal element 1
        matrix = div(matrix, i)
        for k in range(i + 1, n):
            c = matrix.iloc[k, i]
            for j in range(len(matrix.columns)):
                matrix.iloc[k, j] = matrix.iloc[k, j] - matrix.iloc[i, j] * c
    return matrix    

def Diagonolize(matrix):
    n = len(matrix.index)
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            c = matrix.iloc[j, i]
            for k in range(len(matrix.columns)):
                matrix.iloc[j, k] = matrix.iloc[j, k] - c * matrix.iloc[i, k]
    return matrix

def solve(matrix):
    # Convert the augmented matrix into upper triangular form
    matrix = UpperTriangular(matrix)
    # Diagonalize the matrix
    matrix = Diagonolize(matrix)
    # Extract the solution
    solution = matrix.iloc[:, -1].values
    return solution

if __name__ == "__main__":
    matrix = input_matrix()
    print("Input Matrix (Augmented):")
    print(matrix)
    solution = solve(matrix)
    print("Solution:")
    print(solution)
