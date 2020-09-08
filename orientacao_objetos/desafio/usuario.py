class Usuario:
    # matricula, nome, tipo (leitor ou redator), email (CRUD)
    def __init__(self, matricula, nome, tipo, email):
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo #Leitor ou Redator
        self.email = email
        
    #sobreescrevendo o __str__
    def __str__(self):
        return "%d - %s" % self.matricula, self.nome    
    