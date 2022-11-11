def alteralinha(nametxt,inteiro,string):
  file=open(nametxt,"r")#abre um arquivo  como leitura
  lista=[]
  for linha in file.readlines():# le esse arquivo
    var=linha.split("\n") #guarda ele uma variavel: var removendo a lnha
    lista.append(var[0]) # aaiciona os elemento na lista
  file.close()
  lista[inteiro -1]=string # altera o valor de um elemento da lista, com base no valor enviado pelo usuario
  file=open(nametxt,"w")
  for x in range(len(lista)): #apaga todos elementos do arquivo e rescreve com a altercao, colocando quebra de linha
    file.write("%s\n"%(lista[x]))
  file.close()
#esse modulo foi feito para alterar aqrquivos mantendo seus componentes e alterando a linha desejada com base em um valor enviado
#alteralinha("text.txt",4,"valor a mudar na linha")
#SINTAXE

#alteralinha("o diretorio do arquivo, por exemplo text.txt",a linha que deseja mudar em int,"o texto que vai ser alternado na linha desejada, em str")

def deco(cpf):
  pedidos={ #faco um dicionario onde guarda os o valores e nome dos pedidos  pelo chave codigo produto
    "1":[10.00,"X-SAlada"],
    "2":[10.00,'X-Burguer'],
    "3":[7.50,'Cachorro Quente'],
    "4":[8.00,'Misto Quente'],
    "5":[5.50,'Salada de Frutas'],
    "6":[4.50,'Refrigerante'],
    "7":[6.25,'Suco Natural']
  }
  pedido=open("PEDIDO.txt","r")
  for linha in pedido.readlines(): # intuito. preciso pegar a linha onde esta o cpf do cliente
    linha_lista=linha.split("-") # varro o arquivo guardo a primeira linha em um variavel, desmebro ela com o split
    if linha_lista[0]==cpf: #e verefico se o cpf presente nesta linha é o do usuario
      lista_original= linha_lista #se for, guardo esta linha na linha original, com essa linha tenho o que o usuario pediu
  pedido.close()
  for x,y,z in zip(lista_original[1],lista_original[2],lista_original[3]): #como ja tenho a lista pronta,leio codigo por codigo e printo como a chave do dicionario fosse o elemento da lista,arquivo. `
    #coloco duas variaveis no for, o x representa o codigo do produto, e o y a quantidade deste, como o for esta sendo com duas variaveis a quantidade é funcao do seu codigo do produto
    if z=="1":
      print("%1s -  %15s -  Preco Unitario:  R$ %2.2f  Valor: + R$ %.2f" %(y,pedidos[x][1],pedidos[x][0],int(y)*pedidos[x][0]))
    if z=="0":
      print("%1s -  %15s -  Preco Unitario:  R$ %2.2f  Valor: - R$ %.2f - cancelado" % (y, pedidos[x][1], pedidos[x][0],int(y)*pedidos[x][0]))


def procura_linha_cpf(cpf): #este modulo procura no pedido on esta o cpf e retona a linha,lista, do cpf corespondente
  pedido = open("PEDIDO.txt", "r")
  for linha in pedido.readlines():  # intuito. preciso pegar a linha onde esta o cpf do cliente
    linha_lista = linha.split("-")  # varro o arquivo guardo a primeira linha em um variavel, desmebro ela com o split
    if linha_lista[0] == cpf:  # e verefico se o cpf presente nesta linha é o do usuario
      lista_original = linha_lista  # se for, guardo esta linha na linha original, com essa linha tenho o que o usuario pediu
  pedido.close()
  return lista_original

def data():
  import datetime #importo a blibioteca de data
  agora = datetime.datetime.now() #pego a data atual com ano,mes,dia hora,minuto,segundo e milisegundos
  a = str(agora).split(".") #formato apenas para o necessario, data e hora, minunto
  momento = "%s/%s/%s %s,"%(a[0][8:10],a[0][5:7],a[0][0:4], a[0][11:16])
  return momento #retorno ele formato para onde foi chamado


