from Usuario import Usuario

usuarios = []


def main():

    resposta = "s"

    while(resposta == "s"):

        dados = {
            "nome": str(input("Digite nome do usuario: ")),
            "apelido": str(input("Digite nome do apelido: ")),
            "cargo": str(input("Digite nome do cargo: ")),
            "nivel": str(input("Digite nome do nivel: ")) 
        }
        if(validate(dados)):
            usuarios.append(dados)
        else:
            print("Apelido existente!")

        
        print("\n")

        for user in usuarios:
            print(user)    

        print("\n")

        resposta = str(input("\n\nDeseja continuar?"))


def validate(dados):

    for user in usuarios:
        if(user['apelido'] == dados['apelido']):
            return False

    return True        

main()