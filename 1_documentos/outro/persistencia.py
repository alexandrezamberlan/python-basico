from noticia import Noticia

class Persistencia:
    
    @staticmethod
    def gravar(noticia):
        try:
            with open("noticias.csv", "a", encoding='utf8') as escritor:
                #identificador;titulo;categoria;texto;palavra_chave1;palavra_chave2;palavra_chave3
                escritor.write(noticia.identificador + ';' + noticia.titulo + ";" + noticia.categoria + ";" + 
                noticia.texto + ';' + noticia.palavras_chave[0] + ';' + noticia.palavras_chave[1] +
                ';' + noticia.palavras_chave[2])
        except:
            pass

    @staticmethod
    def conectar_base(lista):
        try:
            with open("noticias.csv", "r", encoding='utf8') as leitor:
                dados_linha = []
                for linha in leitor:
                    dados_linha = linha.split(';')
                    noticia = Noticia(dados_linha[0], dados_linha[1], dados_linha[2], dados_linha[3], dados_linha[4], dados_linha[5], dados_linha[6])
                    lista.append(noticia)
                return dados_linha[0]
        except:
            pass
        return 0