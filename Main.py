import os, time
from time import gmtime, strftime


usuarios = []


def insert():

    os.system('cls' if os.name == 'nt' else 'clear')
    dados = {
        "nome": str(input("Digite nome do usuario: ")),
        "apelido": str(input("Digite nome do apelido: ")),
        "cargo": str(input("Digite nome do cargo: "))
    }
    
    escolhas = {
        0: 'visitante',
        1: 'usuario', 
        2: 'adminsitrativo', 
        3: 'técnico ', 
        4: 'super usuario',
    }
    
    print("\nEscolha um nível de acesso para usuário: ")

    for i in range(0, 4):
        print(str(i) + ". " + escolhas.get(i))

    op = int(input("\nDigite qual das opções: "))    
    dados['nivel'] = escolhas.get(op)

    if(validate(dados)):
        dados['data_cadastro'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        usuarios.append(dados)
        
    else:
        print("Apelido existente!")

    print("\n")
  
    print('!!! Usuário inserido')
    time.sleep(2)
    main()


def validate(dados):

    for user in usuarios:
        if(user['apelido'] == dados['apelido']):
            return False

    return True        


def lista():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Todos usuários")

    for user in usuarios:
        print(user)

    time.sleep(5)
    main()    


def find():
    os.system('cls' if os.name == 'nt' else 'clear')
    user_name = str(input("Digite o apelido do usuario que deseja buscar: "))
    for user in usuarios:
        if(user.get('apelido') == user_name):
            print(user)
            

def main():
    
    opcoes = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. para inserir um usuário: ")
    print("2. para listar todos usuários: ")
    print("3. para buscar um usuário: ")
    opcoes = int(input("\nDigite a opção: "))
    
    if(opcoes == 1):
        insert()  
    elif(opcoes == 2): 
        lista()   
    else:
        find()    

main()