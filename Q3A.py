import numpy as np
from fractions import Fraction
from typing import List, Tuple

# This is a script for finding the absorption probabilities of an absorbing markov chain
# Created as a submission to Google Foobar challenge question 3A

#  Q|R
#  ---
#  0|I

# Turn the matrix P into a canonical matrix by moving all absorbing rows to the bottom
# while preserving the ordering
def canonical(P: List[List]) -> Tuple[List[List], int]:
    # Check for the condition of the first row being absorbing
    if sum(P[0]) == 0:
        return None, -1
    # Create lists for the terminal and transcient rows and their original indices
    absorbant_rows, transient_rows = [[], []], [[], []]
    for i, n in enumerate(P):
        if sum(n) == 0:
            absorbant_rows[0].append(n)
            absorbant_rows[1].append(i)
        else:
            transient_rows[0].append(n)
            transient_rows[1].append(i)

    # Build the new matrix with the lists of old rows and indices
    updated_rows = [[transient_rows[0] + absorbant_rows[0]], [transient_rows[1] + absorbant_rows[1]]]
    canonical_matrix = []
    for i, row in enumerate(updated_rows[0][0]):
        new_row = []
        for p in updated_rows[1][0]:
            new_row.append(row[p])
        canonical_matrix.append(new_row)
    
    # Find the denominators of the new rows in the canonical matrix
    den = [float(sum(row)) for row in canonical_matrix]
    
    # Find the number of transient rows and turn all matrix elements into integer ratios
    transient = 0
    for i, n in enumerate(canonical_matrix):
        if den[i] == 0:
            continue
        transient += 1
        for j, k in enumerate(n):
            canonical_matrix[i][j] = k / den[i]
    
    # Return the new matrix, the denominators list, and the terminal rows list
    return canonical_matrix, transient

# Create a fundamental matrix from a canonical matrix using the following formula:
#      N = (I-Q)^-1, 
#           - I is an identity matrix of equal dimensions to Q
#           - Q is the t x t slice of the canonical matrix c
def fundamental(c: np.ndarray, transient_rows: int) -> np.ndarray:
    Q = c[:transient_rows,:transient_rows]
    I = np.zeros(Q.shape, dtype=float)
    for i in range(len(I)):
        I[i, i] = 1.0
    Q = Q.astype('float')
    I = I.astype('float')
    return np.linalg.pinv(I - Q)


def solution(m):
    # Create an equivalent but canonical matrix from m
    canonical_matrix, transient_rows = canonical(m)

    # t will be -1 if the first row of m is absorbing
    if transient_rows == -1:
        answer = [1]
        for i in range(1, len(m)):
            if sum(m[i]) == 0:
                answer.append(0)
        answer.append(1)
        return answer
    
    # Convert the canonical matrix to a numpy array
    Q = np.array(canonical_matrix, dtype=object)

    # Create a fundamental matrix from a copy of Q
    N = fundamental(Q.copy(), transient_rows)

    # Create R, which is a r x t slice from the canonical matrix
    R = Q[:transient_rows,transient_rows:]

    # Find the absorption probability matrix
    B = np.matmul(N, R)

    # The answer to this problem lies in the top row of the matrix
    # These numbers are currently floats, so I need to extract an integer ratio from these decimal approximations\
    # Thankfully the native fractions library has a limit_denominator function that is forgiving of
    # this precision issue
    d, fr  = [], []
    for col in B[0]:
        f = Fraction(col).limit_denominator()
        if f.numerator != 0:
            d.append(f.denominator)
        fr.append((f.numerator, f.denominator))
    
    # Find the least common multiple among the denominators of the non-zero fractions
    l = np.lcm.reduce(np.array(d, dtype=int))

    # The answer can be found using these fractions and the least common multiple of the denominators
    answer = []
    for f in fr:
        answer.append(int(f[0] * (l / f[1])))
    answer.append(l)

    # Reduce the answer to its smallest form
    g = np.gcd.reduce(answer)
    for i, n in enumerate(answer):
        answer[i] = int(n / g)
    return answer

if __name__ == "__main__":
    m1 = [
        [0, 0, 0, 0, 0, 0],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    smalltest = [
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    edge_case1 = [
        [0, 1, 2],
        [0, 0, 0],
        [0, 0, 0],
    ]
    print(solution(m1))
    print(solution(edge_case1))