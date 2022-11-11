from __future__ import with_statement
import os

class Palavra:
  valor = ""
  quantidade = 0

  def __init__(self, valor):
    self.valor = valor
    self.quantidade = 1
    
  def __eq__(self, other):
    if isinstance(other, Palavra):
        return self.valor == other.valor
    return False
    
  def __gt__(self, other):
    if self.quantidade == other.quantidade:
        return self.valor < other.valor
    return self.quantidade > other.quantidade

################################################
class Util:
  @staticmethod
  def abrir_arquivo_texto():
    nome_arquivo = input("Digite caminho e nome do arquivo texto: ")
    print("\n")
    try:
      with open(nome_arquivo, "r", encoding='utf8') as leitor:
          for linha in leitor:
              print(linha)
    except:
      print("Arquivo com problema ou não localizado")
    
    return nome_arquivo
  
  @staticmethod
  def criar_lista_palavras(lista_palavras, nome_arquivo):
    try:
      with open(nome_arquivo, "r", encoding='utf8') as leitor:
          for linha in leitor:
            
            linha = linha.replace(".","")
            linha = linha.replace(";","")
            linha = linha.replace(",","")
            linha = linha.replace("!","")
            linha = linha.replace("?","")
            linha = linha.replace("\n","")
            
            dados_linha = linha.split(" ")
           
            for palavra in dados_linha:
              palavra = palavra.lower()
              
              palavra_oo = Palavra(palavra)

              encontrado = False
              for p in lista_palavras:
                if (p.valor == palavra_oo.valor):
                  p.quantidade += 1
                  encontrado = True   
                
              #saindo do 2n for, significa que palavra_oo nao esta na lista, vamos adiciona-la 
              if (not encontrado):
                lista_palavras.append(palavra_oo)          
    except:
      print("Arquivo com problema ou não localizado")

  @staticmethod
  def exibir_lista_palavras(lista_palavras):
    for palavra in lista_palavras:
      print(palavra.valor, " - ", palavra.quantidade)

#######################################
## parte principal do sistema
  
lista_palavras = []
nome_arquivo = ""

while (True):
  # os.system("clear")
  print("MENU")
  print("1 - Carregar arquivo texto")
  print("2 - Listar palavras e suas ocorrências")
  print("3 - Sair")
  opcao = int(input("Opção: "))

  if (opcao == 1):
    print("Abrindo o arquivo....")
    nome_arquivo = Util.abrir_arquivo_texto()
  elif (opcao == 2):
    print("Lista de palavras....")
    if (nome_arquivo == ""):
      print("Primeiro use a opção 1, para carregar o arquivo texto")
    else:
      lista_palavras.clear()
      Util.criar_lista_palavras(lista_palavras, nome_arquivo)
      lista_palavras.sort(reverse=True)
      Util.exibir_lista_palavras(lista_palavras)
  elif (opcao == 3):
    print("Obrigado por usar o sistema")
    break
  else: 
    print("Opção inválida!")

  # os.system("sleep 4")