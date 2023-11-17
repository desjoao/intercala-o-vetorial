A = [0]*10
B = [0]*10
C = [0]*20

for i in range(10):
    A[i] = int(input(f'Insira o {i+1}º valor do vetor A: '))
    B[i] = int(input(f'Insira o {i+1}º valor do vetor B: '))
    if i == 0:
        C[i] = A[i]
        C[i + 1] = B[i]
    else:
        C[2*i]= A[i]
        C[2*i+1] = B[i]
        

print(C)
