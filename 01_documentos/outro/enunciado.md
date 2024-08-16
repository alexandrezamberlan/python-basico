A notícia deve ter título, categoria (esporte, política, entretenimento), texto (400 letras no máximo) e palavras-chave (3 obrigatoriamente).
O sistema deve permitir que um usuário cadastre, altere, pesquise e remova uma notícia, que deve ser persistida em arquivo .csv (titulo;categoria;texto;palavras-chave).

Para pesquisar, alterar ou remover uma notícia, deve haver um campo que o usuário o preencha. O sistema deve analisar título, categoria, texto e palavras-chave de todas as notícias cadastradas para efetuar a pesquisa, ou a alteração, ou remoção.

Para ajudar:
- criar classe Noticia (titulo, categoria, texto e palavras-chave)
- usar lista
- usar arquivo


Classes
    - Noticia
        - int identificador
        - string titulo
        - string categoria
        - string texto
        - lista de string palavras_chave (validar 3 palavras)

    - Persistencia
        - gravar_noticia()
        - conectar_base()

        - arquivo noticias.csv (identificador;titulo;categoria;texto;palavra_chave1;palavra_chave2;palavra_chave3)

Menu
1 - Cadastrar
2 - Alterar (campo de pesquisa olhando para titulo, categoria, texto e palavras_chave)
3 - Pesquisar (campo de pesquisa olhando para titulo, categoria, texto e palavras_chave)
4 - Remover (campo de pesquisa olhando para titulo, categoria, texto e palavras_chave)
5 - Sair
Opção: 