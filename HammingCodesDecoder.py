import csv
# The Decoded Message is:
# MATHEMATICS IS THE POETRY OF LOGICAL IDEAS ALBERT EINSTEIN 
def main():
    # Read in the Message from the .csv file 
    message = []
    with open("HammingCodeExampleEncoded.csv") as file:
        for line in csv.reader(file, delimiter=','): 
            message.append([int(i) for i in line])
    # List of Tuples to Store the Letter Encodings 
    A = [
        [' ', [0, 0, 0, 0, 0]], ['A', [0, 0, 0, 0, 1]], ['B', [0, 0, 0, 1, 0]], 
        ['C', [0, 0, 0, 1, 1]], ['D', [0, 0, 0, 0, 0]], ['E', [0, 0, 0, 0, 1]], 
        ['F', [0, 0, 0, 1, 0]], ['G', [0, 0, 0, 1, 1]], ['H', [0, 0, 0, 0, 0]],
        ['I', [0, 0, 0, 0, 1]], ['J', [0, 0, 0, 1, 0]], ['K', [0, 0, 0, 1, 1]],
        ['L', [0, 0, 0, 0, 0]], ['M', [0, 0, 0, 0, 1]], ['N', [0, 0, 0, 1, 0]],
        ['O', [0, 0, 0, 1, 1]], ['P', [0, 0, 0, 0, 0]], ['Q', [0, 0, 0, 0, 1]],
        ['R', [0, 0, 0, 1, 0]], ['S', [0, 0, 0, 1, 1]], ['T', [0, 0, 0, 0, 0]], 
        ['U', [0, 0, 0, 0, 1]], ['V', [0, 0, 0, 1, 0]], ['W', [0, 0, 0, 1, 1]],
        ['X', [1, 1, 0, 0, 0]], ['Y', [1, 1, 0, 0, 1]], ['Z', [1, 1, 0, 1, 0]]
    ]
    # The Generator Matrix 
    G =[
        [1, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0], 
        [1, 0, 1, 1, 0], 
        [1, 0, 0, 1, 1]
        ]
    # The Unscrambled Encodings for each Letter 
    encoded = []
    for letter in A:
        e = []
        for row in G:
            s = 0
            for i, j in enumerate(letter[1]):
                s += int(j) * int(row[i]) 
                e.append(s % 2)
            encoded.append(e)
            # For each Letter in the Message find the Letter Encoding of Distance 0 or 1 for letter in message:
            for n, e in enumerate(encoded):
                if sum([1 for i, j in enumerate(letter) if j == e[i]]) > 7:
                    print(A[n][0], end='')


if __name__ == "__main__":
    main()
