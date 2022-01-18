#Method for user adding of matrix lines and columns
def ln_col(num):
    try:   
        print("How many lines will",f"matrix {num} have?")
        ln = int(input())
        print("How many columns will",f"matrix {num} have?")
        col = int(input())
        out = (ln,col)
        return out        
    #Exception for working with integers
    except ValueError:
        print("You didn't enter a integer.")
        exit()

#Method for user adding of matrix elements
def elements(ln,col,num):
    mat = []
    for i in range(ln):
        l = []
        print("Enter elements of",f"{i+1}. line of matrix {num}.") 
        print("After enter one element press ENTER.")
        for j in range(col):
            inp = str(input())
            ot = 'False'
            #Fractions (for example: 1/4) accepting
            try:    
                for lom in range(len(inp)):
                    if inp[lom] == '/':
                        x =float(inp[:lom])
                        y = float(inp[(lom+1):])
                        l.append(x/y)
                        ot = 'True'
                if ot == 'False':
                    l.append(float(inp))
            #Exception for working with numbers
            except ValueError:
                print("You didn't enter a number.")
                exit()    
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
    mat = []
    #Creating Zero matrix
    for i in range(len(matA)):
        o = []
        for j in range(len(matB[0])):
            o.append(0)
        mat.append(o)
    #Calculing elements
    for i in range(len(matA)):
        for j in range(len(matB[0])):
            for k in range(len(matB)):
                mat[i][j] += matA[i][k] * matB[k][j]
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
    print("Count of the first matrix columns isn't a equal to count of the second matrix lines.")
    exit()

#Calling method for user adding matrix elements
matA = elements(ln_A,col_A,1)
matB = elements(ln_B,col_B,2)

#Calling method for calculing matrix multiplication
matC = calc(matA,matB)

#Matrixs printing
print()
print("Result multiplication of this matrix:")
print_mat(matA)
print()
print("and this matrix:")
print_mat(matB)
print()
print("is this matrix:")
print_mat(matC)