#Funcionando percorrer o arquivo csv
myfile = open("file.csv", "r")
while myfile:
    line  = myfile.readline()
    # print(line)
    registro = line.split(';')

    print(f'DRT: {registro[0]}')
    print(f'Nome: {registro[1]}')
    print(f'Cargo: {registro[2]}')
    print(f'Perfil_Acesso: {registro[3]}')

    if line == "":
        print(f'{registro[0]}')
        break
myfile.close() 
