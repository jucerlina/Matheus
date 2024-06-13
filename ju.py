sala=[]
for nome in range (1,30):    
    nome=str(input("um nom de aluno:"))
    sala.append(nome) 
    if ((nome)=="fim") :
        sala.pop(-1)
        break
    print(sala)