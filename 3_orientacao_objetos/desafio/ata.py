class Ata:
    def __init__(self, numero, data, hora, local, pauta):
        self.numero = numero
        self.data = data 
        self.hora = hora
        self.local = local
        self.pauta = pauta
        self.redador = None
        self.texto = None
        self.lista_integrantes = []
        self.validade = None
        
    def __str__(self):
        return "%s - %s" % (self.numero, self.data)
        
        
        