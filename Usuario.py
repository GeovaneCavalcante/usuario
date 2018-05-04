
class Usuario(object):

    nome = ""
    apelido = ""
    cargo = ""
    nivel = ""

    def __init__(self, nome, apelido, cargo, nivel):
        
        self.nome = nome
        self.apelido = apelido
        self.cargo = cargo
        self.nivel = nivel
    
        