#Funcionando e adicionando usuários
from usuario.models import Usuario

myfile = open("file.csv", "r")
while myfile:
    line  = myfile.readline()
    # print(line)
    registro = line.split(';')

    print(f'DRT: {registro[0]}')
    print(f'Nome: {registro[1]}')
    print(f'Cargo: {registro[2]}')
    print(f'Perfil_Acesso: {registro[3]}')
    user = Usuario(drt= registro[0], nome= registro[1], cargo= registro[2], perfil_acesso= registro[3])
    user.save()

    if line == "":
        print(f'{registro[0]}')
        break
myfile.close() 
