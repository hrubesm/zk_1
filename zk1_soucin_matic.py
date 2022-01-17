#Method for user adding of matrix lines and columns
def ln_col(num):
    try:   
        print("Kolik řádků bude mít",f"matice {num}?")
        ln = int(input())
        print("Kolik sloupců bude mít",f"matice {num}?")
        col = int(input())
        out = (ln,col)
        return out
        
    #Exception for working with integers
    except ValueError:
        print("Nezadal jste celé číslo.")
        exit()

#Method for user adding of matrix elements
def elements(ln,col,num):
    mat = []
    for i in range(ln):
        l = []
        print("Zadejte hodnoty",f"{i+1}. řádku matice {num}.") 
        print("Po zadání hodnoty stiskněte ENTER")
        for j in range(col):
            inp = str(input())
            ot = 'False'

            #Fractions (for example: 1/4) accepting
            for lom in range(len(inp)):
                if inp[lom] == '/':
                    x =float(inp[:lom])
                    y = float(inp[(lom+1):])
                    l.append(x/y)
                    ot = 'True'
            if ot == 'False':
                l.append(float(inp))
        mat.append(l)
    ot = 'False'    
    return mat

#Method for matrix printing
def print_mat(mat):
    for i in range(len(mat)):
        print("[",end = "")
        for j in range(len(mat[i])-1):
            print(mat[i][j]," ",end = "")
        print(mat[i][-1],end = "")
        print("]")

#Method for calculing matrix multiplication
def calc(matA,matB):
    j = 0
    o = []
    for _ in range(len(matB[0])):
        p = []
        c = 0    
        for i in range(len(matB)):
                p.append(matB[i][j])
        for k in range(len(matA)):
            c = 0
            for i in range(len(matB)):
                    c += (matA[k][i] * p[i]) 
            o.append(c)   
        j += 1
    return o

#Method for indexs of matrix multiplication
def idxing(o,ln_A):
    counter = 0
    mat = []
    for _ in range(ln_A):
        q = []
        for x in range(len(o)):
            if x%(ln_A) == counter:
                q.append(o[x])
        counter += 1
        mat.append(q)
    return mat

#Calling method for user adding matrix lines and columns 
out_A = ln_col(1)
out_B = ln_col(2)
ln_A = out_A[0]
col_A = out_A[1]
ln_B = out_B[0]
col_B = out_B[1]

#Condition of matrix multiplication -> count of the first matrix columns must be a equal to count of the second matrix lines
if col_A != ln_B:     
    print("Počet sloupců první matice neodpovídá počtu řádků druhé matice.")
    exit()

#Calling method for user adding matrix elements
matA = elements(ln_A,col_A,1)
matB = elements(ln_B,col_B,2)

#Calling method for calculing matrix multiplication
elmts_matC = calc(matA,matB)

#Calling method for indexs of matrix multiplication
matC = idxing(elmts_matC,ln_A)

#Matrixs printing
print()
print("Výsledek součinu této matice:")
print_mat(matA)
print()
print("a této matice:")
print_mat(matB)
print()
print("je:")
print_mat(matC)