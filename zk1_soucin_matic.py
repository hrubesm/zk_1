

try:
    with open ('mat_A.txt', encoding="utf-8") as A,\
        open ('mat_B.txt', encoding="utf-8") as B,\
        open ('mat_C',"w", encoding="utf-8") as C:
        readerA = A.readlines()
        readerB = B.readlines()
    print(readerA)
    print(len(readerA))
    print(readerB)
    print(len(readerB))


    #Naplnění matic, resp. seznamy seznamů čísly vč. ošetření, že se jedná o čísla
    matA = []
    matB = []
  
    for i in range (len(readerA)):
        l = []
        for j in range(len(readerA[i])):
            if readerA[i][j] == " ":
                continue
            elif readerA[i][j] == "\n":
                matA.append(l)
                print("Konec řádku")
                break
            else:
                try:
                    try:
                        print(readerA[i][j])
                        c = readerA[i][j]+readerA[i][j+1]
                        l.append(float(c))
                        print("zde je c",c)
                        j = 
                    except ValueError:                                               
                        l.append(float(readerA[i][j]))
                        print("ahojík")
                        pass
                    except IndexError:
                        pass   
                       
                       
                except ValueError:
                    print(readerA[i][j],"Je toto mezera?")
                    print("V matici A se na pozici",i+1,"řádku a",int(j/2)+1,"sloupce se nenachází číslo.")
                    exit()
    matA.append(l)
    print("konec řádku")
    for i in range (len(readerB)):
        l = []
        for j in range(len(readerB[i])):
            if readerB[i][j] == " ":
                continue
            elif readerB[i][j] == "\n":
                matB.append(l)
                break
            else:
                try:
                    l.append(float(readerB[i][j]))
                except ValueError:
                    print(readerB[i][j],"Je toto mezera?")
                    print("V matici B se na pozici",i+1,"řádku a",int(j/2)+1,"sloupce se nenachází číslo.")
                    exit()
    matB.append(l)

    print(matA)
    print(matB)
    print(len(matA))
    print(len(matA[0]))


    #Ošetření obdélníkovosti matic
    i = 0
    for i in range(len(matA[i])):
        if len(matA[0]) != len(matA[i]):
            print("Matice A není obdelníková")
            exit()
    for i in range(len(matB[i])):
        if len(matB[0]) != len(matB[i]):
            print("Matice B není obdelníková")
            exit()
    print("Ahoj")

    #Výpočet matice C
    matC = []
    i = 0
    
    soucet = 0
    for i in range(len(matA[i])):
        print(i,"vnější")
        j = 0
        for i in range(len(matB[i])):    
            print(j)
            l = []
            
    
            soucet += (matA[i][j]*matB[i][j])
            print(matA[i][j],matB[j][i],"sou",soucet)
            j += 1
            l.append(soucet)
        soucet = 0
        matC.append(l)
    

    print(matC)

except IOError:
    print("Chyba při načtení souboru.")
    