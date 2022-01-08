#Zadávání počtů řádků a sloupců obou matic
try:   
    print("Kolik řádků bude mít první matice?")
    rad_A = int(input())
    print("Kolik sloupců bude mít první matice?")
    slou_A = int(input())
    print("Kolik řádků bude mít druhá matice?")
    rad_B = int(input())
    if slou_A != rad_B:
        print("Počet sloupců první matice neodpovídá počtu řádků druhé matice.")
        exit()
    print("Kolik sloupců bude mít druhá matice?")
    slou_B = int(input())
except ValueError:
    print("Nezadal jste celé číslo.")
    exit()


#Zadávání konkrétních hodnot do matic
matA = []
matB = []
for i in range(rad_A):
    l = []
    print("Zadejte hodnoty",i+1,"řádku první matice. Po zadání hodnoty stiskněte ENTER")
    for j in range(slou_A):
        inp = str(input())
        ot = 'False'
        for lom in range(len(inp)):
            if inp[lom] == '/':
                x =float(inp[:lom])
                y = float(inp[(lom+1):])
                l.append(x/y)
                ot = 'True'
        if ot == 'False':
            l.append(float(inp))
    matA.append(l)
ot = 'False'
for i in range(rad_B):
    l = []
    print("Zadejte hodnoty",i+1,"řádku druhé matice. Po zadání hodnoty stiskněte ENTER")
    for j in range(slou_B):
        inp = str(input())
        ot = 'False'
        for lom in range(len(inp)):
            if inp[lom] == "/":
                x =float(inp[:lom])
                y = float(inp[(lom+1):])
                l.append(x/y)
                ot = 'True'
        if ot == 'False':
            l.append(float(inp))
    matB.append(l)
print(matA,"Matice A")
print(matB,"Matice B")


#Výpočet hodnot matice součinu umístěných do jednoho seznamu
matC = []
o = []
c = 0
j = 0
k = 0
for _ in range (slou_B):
    p = []
    c = 0    
    for i in range(rad_B):
        #try:
            p.append(matB[i][j])
        #except IndexError:
            #pass
    for _ in range (rad_A):
        c = 0
        for i in range(rad_B):
            #try:
                c += (matA[_][i] * p[i])
                print(matA[_][i],p[i],c)    
            #except IndexError:
                #pass
        o.append(c)   
    j += 1

#Přeindexování seznamu hodnot matice součinu, tak aby odpovídala její struktuře řádků a sloupců
citac = 0
for _ in range(rad_A):
    q = []
    for x in range(len(o)):
        if x%(rad_A) == citac:
            q.append(o[x])
    citac += 1
    matC.append(q)

#Vytisknutí matice

print("ODTUD UŽ TISKNEME NAOSTRO!")
for i in range(len(matC)):
    print("[",end = "")
    for j in range(len(matC[i])-1):
        print(matC[i][j]," ",end = "")
    print(matC[i][-1],end = "")
    print("]")