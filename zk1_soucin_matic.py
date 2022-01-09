#Zadávání počtů řádků a sloupců obou matic:
try:   
    print("Kolik řádků bude mít první matice?")
    rad_A = int(input())
    print("Kolik sloupců bude mít první matice?")
    slou_A = int(input())
    print("Kolik řádků bude mít druhá matice?")
    rad_B = int(input())
    
    #Podmínka, kterou je potřeba splnit, aby bylo možné matice (v tomto pořadí) dát do součinu:
    # -> Počet sloupců první matice se musí rovnat počtu řádků druhé matice.
    # -> V případě nesplnění dojde k oznámení o nesplnění podmínky a k ukončení programu.
    if slou_A != rad_B:     
        print("Počet sloupců první matice neodpovídá počtu řádků druhé matice.")
        exit()
    print("Kolik sloupců bude mít druhá matice?")
    slou_B = int(input())

#Vyjímka zajišťující práci s celočíselnými počty řádků a sloupců
except ValueError:
    print("Nezadal jste celé číslo.")
    exit()


#Zadávání konkrétních hodnot do matic:
#Uživatel zadává vždy hodnoty jednoho řádku (pro každé zapsání hodnoty je potřeba zmáčknout ENTER), které se ukládají jako seznam hodnot.
#Program akceptuje i zlomky (hodnoty s lomítkem), např: 1/4.
#Po naplnění se řádku (list 'l') se tento seznan uloží do proměné matA, resp. matB, vyprázdní se a postup se opakuje.
#Výsledná proměnná matice je tedy seznam seznamů reálných čísel.
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


#Výpočet hodnot matice součinu, které jsou následně umístěné do jednoho seznamu 'o':
#Nejprve je z každého řádku druhé matice ('matB') vybrána hodnota s daným indexem, která se ukládá do seznamu 'p'.
#Po naplnění seznamu 'p' se pak každá idexovaná hodnota ze seznamu 'p[i]' vynásobí s každou indexovanou hodnotou daného řádku první matice ('matA').
#Tyto vynásobené hodnoty pro jeden řádek první matice se následně sečtou dohromady (do proměnné 'c') a výsledek se uloží do seznamu 'o'.
#Následně se seznam 'p' vyprázdní a postup se opakuje.
matC = []
o = []
c = 0
j = 0
k = 0
for _ in range(slou_B):
    p = []
    c = 0    
    for i in range(rad_B):
            p.append(matB[i][j])
    for _ in range (rad_A):
        c = 0
        for i in range(rad_B):
                c += (matA[_][i] * p[i]) 
        o.append(c)   
    j += 1


#Přeindexování hodnot seznamu 'o', tak aby odpovídaly struktuře řádků a sloupců výsledné matice součinu:
#Všechny hodnoty ze seznamu 'o' procházejí for cyklem, kde se program ptá na výsledek podílu indexu hodnoty ('x') a počtem řádků první matice ('radA')
#Pokud výsledek odpovídá proměnné 'citac', hodnotnota se uloží do seznamu 'q'
#Na konci se proměnná 'citatc' zvýší o 1 a seznam 'q' se uloží do proměnné 'matC'
#Hodnoty seznamu 'q' tedy odpovídají jednomu řádků nově vytvořené matice, která je součinem zadaných matic.
citac = 0
for _ in range(rad_A):
    q = []
    for x in range(len(o)):
        if x%(rad_A) == citac:
            q.append(o[x])
    citac += 1
    matC.append(q)

#Vytisknutí matic a jejich součinu:
#Protože výstupní hodnoty jsou vypisovány v terminálu programu, byl jejich výpis pro přehlednost upraven.
#Každá hodnota je od sebe oddělena dvěma mezerami, vyjma krajních hodnot.
print()
print("Výsledek součinu této matice:")
for i in range(len(matA)):
    print("[",end = "")
    for j in range(len(matA[i])-1):
        print(matA[i][j]," ",end = "")
    print(matA[i][-1],end = "")
    print("]")
print()
print("a této matice:")
for i in range(len(matB)):
    print("[",end = "")
    for j in range(len(matB[i])-1):
        print(matB[i][j]," ",end = "")
    print(matB[i][-1],end = "")
    print("]")
print()
print("je:")
for i in range(len(matC)):
    print("[",end = "")
    for j in range(len(matC[i])-1):
        print(matC[i][j]," ",end = "")
    print(matC[i][-1],end = "")
    print("]")