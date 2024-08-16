class Noticia:
    
    # construtor
    # identificador;titulo;categoria;texto;palavra_chave1;palavra_chave2;palavra_chave3
    def __init__(self, identificador, titulo, categoria, texto, palavras_chave):
        self.identificador = identificador
        self.titulo = titulo.upper()
        self.categoria = categoria.upper()
        self.texto = texto
        self.palavras_chave = palavras_chave        

    def __str__(self):
        return f"Notícia: {self.identificador} - {self.titulo} - {self.categoria}"
    
    def __eq__(self, other):
        if isinstance(other, Noticia):
            return self.identificador == other.identificador
        return False

    def __gt__(self, other):
        return self.titulo > other.titulo