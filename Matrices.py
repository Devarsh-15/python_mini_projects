import random

def generate_alternate_matrix(n):
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            num = random.randint(0, 99)
            if (i + j) % 2 == 0:
                row.append(num)
            else:
                row.append(-num)
        A.append(row)
    return A


def generate_second_matrix(A, operation):
    n = len(A)
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            if operation == "add":
                # A + B = 1 → B = 1 - A
                row.append(1 - A[i][j])
            elif operation == "sub":
                # A - B = 1 → B = A - 1
                row.append(A[i][j] - 1)
        B.append(row)
    return B


def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def print_matrix(M, name):
    print(f"\n{name}:")
    for row in M:
        print(row)


n = int(input("Enter n: "))
operation = input("Do you want to (add) or (sub) ? Enter 'add' or 'sub': ").lower()

if operation not in ["add", "sub"]:
    print("Invalid operation!")
    exit()

A = generate_alternate_matrix(n)
B = generate_second_matrix(A, operation)

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

if operation == "add":
    result = add_matrices(A, B)
    print_matrix(result, "Result (A + B)")
else:
    result = subtract_matrices(A, B)
    print_matrix(result, "Result (A - B)")
