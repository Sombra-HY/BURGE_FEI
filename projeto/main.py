#aconselho ler o slide read me, para entender como funciona o gerenciamento de arquivos

from arquivomodulo import alteralinha, procura_linha_cpf, data, deco

def menu_de_opcoes(): #menu de opcoes do pedido
    valor=1
    while True:
        print("""\n1 - Novo Pedido
2 - Cancela Pedido
3 - Insere Produto
4 - Cancela Produto
5 - Valor do Pedido
6 - Extrato do Pedido
     
0 - Sair""")# lista de opcoes
        opcao=input("\nDIGITE A OPÇÃO DESEJADA: ")
        if (opcao.isdigit()) and (opcao in ["1", "2", "3", "4", "5", "6"]): #Se o usuario digitar letras ou numeros nao correspondentes ao mostrado na lista, repetira as opcoes ao usuario,  ou seja duas condicoes precisam ser verdadeiras, ser um numero e esta na lista.
            if opcao=="1":
               Novo_pedido()
            if opcao == "2":
                Cancela_pedido()
            if opcao=="3":
               insere_produto()
            if opcao=="4":
               cancela_produto()
            if opcao == "5":
                valor_pagar()
            if opcao=="6":
               extrato()
        if opcao=="0":
            valor=0
            print("...")
            break
        else:
            print("\nPor favor, digite apenas numeros que estejam nas opcoes!")
            continue

def Novo_pedido():#NOvo pedido
    while True: #looop do nome
        nome=input("Digite seu nome: ").upper()
        if (any(sa.isdigit() for sa in nome)) or  (any(x in ["!","@","-","?","`"] for x in nome)):# caso o usuario digite numeros ou caracteres no nome, ele tera que redigitalos
            continue #essa condicao varre o str nome na procura de um numero, se tiver um retorna true renciando o loop
        else:
            break
    while True:
        cpf = input("Digite seu CPF: ")
        if (cpf.isdigit()): #Aqui fazemos a mesma verificao, so que agora apenas numeros sao aceitos no cpf
            break
        else:
            continue
    senha=input("Digite uma senha: ")
    banco=open("BANCO_DE_DADOS.txt","r")
    lista_nome=[]
    lista_cpf=[]
    lista_senha=[]
    for linha in banco.readlines(): #aqui guardamos todos os dados do arquivo em variaveis, deixando mais organizado.
        var=linha.split("-") #corto a funcao pelo "-" para diferenciar o que é um senha de um cpf etc.
        lista_nome.append(var[0])# As variaveis abaixo sao uma lista com os nomes, cpf, senha em orden
        lista_cpf.append(var[1])
        lista_senha.append(var[2])
    if cpf in lista_cpf: #primeira condicao se o cpf estiver presente do arquivo
        for x in range(len(lista_cpf)):#
            if(nome==lista_nome[x] and cpf==lista_cpf[x] and senha==lista_senha[x]):
                print("Concetando...")
                Menu_do_pedido()
            if((nome!=lista_nome[x]) and (cpf==lista_cpf[x]) and (senha==lista_senha[x])) or ((nome==lista_nome[x]) and (cpf==lista_cpf[x]) and (senha!=lista_senha[x])) or ((nome!=lista_nome[x]) and (cpf==lista_cpf[x]) and (senha!=lista_senha[x])): # esse if vai vereficar se o nome esta igual e a senha, caso nao esteje retorna que esta errado um destes
                print("Nome ou senha Incorretos!")
                Novo_pedido()
    else: #se o cpf nao esta presene no arquivo,entao ele escrevera no banco de dados
        banco=open("BANCO_DE_DADOS.txt","a")
        banco.write("%s-%s-%s-\n"%(nome,cpf,senha)) #esta formatacoa é necessaria para diferenciar o que é um nome de um cpf etc. "nome-cpf-senha-"
        banco.close()
        pedido=open("PEDIDO.txt","a")
        pedido.write("%s-"%(cpf)) # aqui escrevo no pedido o cpf, para garantir uma unica escrita(e para nao ter problemas com variavel local como a funcao sobre o pedido esta mais adiante)
        pedido.close()
        print("\nUsuario Cadastrado!")
        Menu_do_pedido()

def Menu_do_pedido(): # funcao onde printa a tabela de opcaoes de usuarios
    l_codigo="" #aqui defino strings que usarei para guardar os valores do codigo do produto e a quanntidade
    l_quantidade=""
    ativo="" #esta variavel define se produto foi cancelado ou nao, 1 para ativo e 0 para cancelado, inicialmente ele ficara ativo (leia o READ ME)
    while True: #caso o Usuario digite algo errad,por exemplo, uma letra ou um numero nao presente na  lista repetira novamente a lista
        print("""
        _______________________________________________
        | CODIGO |         PRODUTO        |   PREÇO   |
        _______________________________________________
        |    1   |         X-SAlada       |  R$ 10,00 | 
        _______________________________________________
        |    2   |        X-Burguer       |  R$ 10,00 | 
        _______________________________________________
        |    3   |     Cachorro Quente    |  R$ 7,50  | 
        _______________________________________________
        |    4   |      Misto Quente      |  R$ 8,00  | 
        _______________________________________________
        |    5   |     Salada de Frutas   |  R$ 5,50  | 
        _______________________________________________
        |    6   |      Refrigerante      |  R$ 4,50  | 
        _______________________________________________
        |    7   |      Suco Natural      |  R$ 6,25  | 
        _______________________________________________""")
        produto=input("\nDigite o Codigo do produto Desejado: ")
        quantidade=input("\nDigite a quantidade do produto anterior: ")

        if (produto.isdigit()) and (quantidade.isdigit()) and (produto in ["1","2",'3','4','5','6','7']):
            l_codigo+=produto
            l_quantidade+=quantidade
            ativo+="1" #colocara 1 para a qantidade de pedidos, exemplo, suco,refri,hotdog, ficara 111
            def pedido_retorno():   # aqui temos uma sub funcao, que mostrara ao usuario se ele gostaria de retornar no menu ou nao
                print("""
                 
1 - Adicionar mais um produto
2 - Voltar para o Menu""")
                escolha=input("Escolha entre as opções acima:")
                if (escolha.isdigit()) and (escolha in ["1", "2"]):#caso ele digite uma letra ou valor fora do menu, ficara repetindo o que eledeseja fazer
                    if escolha=="1":
                        loop=True
                        return loop #caso ele digite 1, ele podera colocar mais produtos no "carrinho", sera retornado True ativando o loop
                    if escolha=="2": #caso ele digite 2, retornara para o menu, como o usuario nao adcionara mais nada, sera escrito no arquivo, salvando o pedido deste
                        pedido = open("PEDIDO.txt", "a")
                        horario = data()
                        pedido.write("%s-%s-%s-%s-\n"%(l_codigo,l_quantidade,ativo,horario))
                        pedido.close()
                        menu_de_opcoes()
                else:
                    print("Digite apenas numeros validos!")
                    pedido_retorno()
            var_loop=pedido_retorno() # aqui ele recebe o retorno, se for true repete de novo o While preservando as variaveis da lista do codigfo e produto
        if (var_loop):
            continue
        else:
            print("\nPor favor digite apenas numeros, codigos, validos!")

# a funcao login tem como unico proposito apenas logar e retornar true se o usuario escrever o cpf e senha certos, por isso ela sera chamada em varias funcoes como forma de validacao, cancela, insere produto, extrato etc.

def login():
    while True:
        cpf = input("Digite seu CPF: ")
        if (cpf.isdigit()): #verefica se o usuario digitou certo o CPF
            break
        else:
            continue

    senha=input("Digite uma senha: ")
    banco=open("BANCO_DE_DADOS.txt","r")
    lista_nome=[]
    lista_cpf=[]
    lista_senha=[]
    on=0
    for linha in banco.readlines(): #aqui guardamos todos os dados do arquivo em variaveis, deixando mais organizado.
        var=linha.split("-") #corto a funcao pelo "-" para diferenciar o que é um senha de um cpf etc.
        lista_nome.append(var[0])
        lista_cpf.append(var[1])# As listas abaixo, sao uma lista com todos cpfs e todas senha guardadas em varivaeis
        lista_senha.append(var[2])
    if cpf in lista_cpf: #primeira condicao se o cpf estiver presente do arquivo
        for x in range(len(lista_cpf)):#
            if(cpf==lista_cpf[x] and senha==lista_senha[x]):
                print("\nConcetando...")
                on=1
                return [cpf,on,lista_nome[x]] # retorno True e o cpf e o nome associado a este cpf  para trabalhar com estas variaveis nas funcoes a seguir
            if((cpf==lista_cpf[x]) and (senha!=lista_senha[x])): #
                print("senha Incorreta!")
                login()
    else:
        print("CPF nao cadastrado no banco de danos!\n Por favor, Cadastre no menu na opção Novo Pedido! ")
        menu_de_opcoes()

def Cancela_pedido():
    var=login()
    while True:
        if (var[1]==1): #a funcao so é executada se o login for executado com sucesso, ou seja ele retorna 1 no var[1],e var[0]=cpf
            print("""
Deseja mesmo cancelar o pedido?
1 - NAO
2 - SIM""")
            resposta=input(": ")
            if (resposta.isdigit()) and (resposta in ["1","2"]): #caso ele digite um numero que nao seja 1 ou 2, ou que nao seja um digito repetira o input
                if resposta=="1":
                    menu_de_opcoes() #se digitar um retornara para o menu de opcoes
                    break #caso digite irra parar
                if resposta=="2":
                    arquivo=open("PEDIDO.txt","r")
                    som=0
                    for linha in arquivo.readlines(): #busco as linhas no arquivo
                        som+=1 #criar um contador para saber qual linha esta o pedido associado ao login
                        lista_linha=linha.split("-")
                        if (lista_linha[0]==var[0]):# verifico se o cpf da linha no arquivo é igual ao cpf do login
                            alteralinha("PEDIDO.txt",som," - - - - -")# se for apago o pedido do cliente, este modulo esta sendo explicado melhor na pasta correspondente(arquivomodulo.py), em base ele altera a linha em um arquivo subtituindo o valor pelo o enviado pelo usuario mantendo as configs originais
                    arquivo.close()
                    menu_de_opcoes()
            else:
                continue

def insere_produto():
    var=login()
    cpf=var[0]
    if var[1]==1: #esta funcao abaixo é identica ao menu do pedido, mudando apenas na linha 223
        l_codigo = ""  # aqui defino strings que usarei para guardar os valores do codigo do produto e a quanntidade
        l_quantidade = ""
        ativo=""
        while True:  # caso o Usuario digite algo errad,por exemplo, uma letra ou um numero nao presente na  lista repetira novamente a lista
            print("""
                _______________________________________________
                | CODIGO |         PRODUTO        |   PREÇO   |
                _______________________________________________
                |    1   |         X-SAlada       |  R$ 10,00 | 
                _______________________________________________
                |    2   |        X-Burguer       |  R$ 10,00 | 
                _______________________________________________
                |    3   |     Cachorro Quente    |  R$ 7,50  | 
                _______________________________________________
                |    4   |      Misto Quente      |  R$ 8,00  | 
                _______________________________________________
                |    5   |     Salada de Drutas   |  R$ 5,50  | 
                _______________________________________________
                |    6   |      Refrigerante      |  R$ 4,50  | 
                _______________________________________________
                |    7   |      Suco Natural      |  R$ 6,25  | 
                _______________________________________________""")
            produto = input("\nDigite o Codigo do produto Desejado: ")
            quantidade = input("\nDigite a quantidade do produto anterior: ")
            if (produto.isdigit()) and (quantidade.isdigit()) and (produto in ["1", "2", '3', '4', '5', '6', '7']):
                l_codigo += produto
                l_quantidade += quantidade
                ativo+="1"

                def pedido_retorno():  # aqui temos uma sub funcao, que mostrara ao usuario se ele gostaria de retornar no menu ou nao
                    print("""

        1 - Adicionar mais um produto
        2 - Voltar para o Menu""")
                    escolha = input("Escolha entre as opções acima:")
                    if (escolha.isdigit()) and (escolha in ["1","2"]):# caso ele digite uma letra ou valor fora do menu, ficara repetindo o que eledeseja fazer
                        if escolha == "1":
                            loop = True
                            return loop  # caso ele digite 1, ele podera colocar mais produtos no "carrinho", sera retornado True ativando o loop
                        if escolha == "2":  # caso ele digite 2, retornara para o menu, como o usuario nao adcionara mais nada, sera escrito no arquivo, salvando o pedido deste
                            pedido=open("PEDIDO.txt","r")
                            cont=0
                            for linha in pedido.readlines():# passa linha por linha e retorna na variavel linha,o intuito é pegar a linha em que o cpf é a mesma do q o login,ou seja vamos pegar o pedido do usuario com base no cpf
                                cont+=1 # crei um contador para saber qual linha é a atual
                                lista=linha.split("-") #guardamos a linha conforme e separamos ela pelo "-" em uma lista
                                if lista[0]==cpf: # verefica linha por linha na busca da linha do usuario com cpf igual
                                    linha_cpf=lista #por ultimo guarda a linha com o cpf do usuario no linha_cpf, em formato de lista
                                    Cont=cont #e guarda a linha do cpf do usuario
                                    alteralinha("PEDIDO.txt",Cont,"%s-%s%s-%s%s-%s%s-%s-"%(linha_cpf[0],linha_cpf[1],l_codigo,linha_cpf[2],l_quantidade,linha_cpf[3],ativo,linha_cpf[4]))    #agora que tenho o numero da linha, o conteudo dela vou alterar adicionando com o modulo altera linha
                                    #basicamente ele vai adicionar mais elementos nos seus correspondentes, por exemplo, cpf-codigos-qunatidadades-, ficara cpf-codigos+valor-quantidade+valor
                            pedido.close()
                            menu_de_opcoes()

                    else:
                        print("Digite apenas numeros validos!")
                        pedido_retorno()

                var_loop = pedido_retorno()  # aqui ele recebe o retorno, se for true repete de novo o While preservando as variaveis da lista do codigfo e produto
            if (var_loop):
                continue
            else:
                print("\nPor favor digite apenas numeros, codigos, validos!")

def cancela_produto():
    var=login()
    cpf=var[0]
    pedidos = {  # faco um dicionario onde guarda os o valores e nome dos pedidos  pelo chave codigo produto
        "1": [10.00, "X-SAlada"],
        "2": [10.00, 'X-Burguer'],
        "3": [7.50, 'Cachorro Quente'],
        "4": [8.00, 'Misto Quente'],
        "5": [5.50, 'Salada de Frutas'],
        "6": [4.50, 'Refrigerante'],
        "7": [6.25, 'Suco Natural']
    }
    contador=0
    pedido = open("PEDIDO.txt", "r")
    for linha in pedido.readlines():  # intuito. preciso pegar a linha onde esta o cpf do cliente
        linha_lista = linha.split(
            "-")  # varro o arquivo guardo a primeira linha em um variavel, desmebro ela com o split
        contador+=1 #contador de linha
        if linha_lista[0] == cpf:  # e verefico se o cpf presente nesta linha é o do usuario
            lista_original = linha_lista  # se for, guardo esta linha na linha original, com essa linha tenho o que o usuario pediu
            linha_numero= contador
    pedido.close()
    cont=0
    print("\nCodigo")
    for x, y, z in zip(lista_original[1], lista_original[2], lista_original[3]):  # como ja tenho a lista pronta,leio codigo por codigo e printo como a chave do dicionario fosse o elemento da lista,arquivo. `
        # coloco duas variaveis no for, o x representa o codigo do produto, e o y a quantidade deste, como o for esta sendo com duas variaveis a quantidade é funcao do seu codigo do produto
        cont+=1
        if z == "1": #imprimoo os produtos que o cliente ja pediu junto com os cancelados
            print("  %d     Quantidade %s -%15s -" % (cont,y, pedidos[x][1])) #coloco um cont para deixar essse printo com um codigo 1,2,3 etc. para o cancelamento
        if z == "0":
            print("  %d     Quantidade %s -%15s -cancelado" % (cont,y, pedidos[x][1]))
    escolha=input("digite um codigo para cancelar: ")
    lista=procura_linha_cpf(cpf) #guarda a linha com base no cpf que enviei
    stra = "" #apos o usuario digital quel produto deseja cancelar devo alterar a string com indice que foi digitado para zero(zero significa cancelado)
    cont = 0 #defino um contador para saber qual "indice" da strinf estou
    for z in lista[3]: #varro a string do arquivo o que se refere a "ATIVO"= 1111
        cont += 1 #o cont a cada indice do elemento
        if int(escolha) == cont: #caso ele seja igual a inidice que o usuario quer alterar,cancelar, adicione um zero
            stra += "0"
        else:
            stra += z #caso contrario adicione o que ja esta presente
    lista[3] = stra #como nao é possivel alterar uma letra especifica de um strinf crio uma nova string e substituo na lista com as alteracoes
    alteralinha("PEDIDO.txt",linha_numero,"%s-%s-%s-%s-%s-"%(lista_original[0],lista_original[1],lista_original[2],lista[3],lista_original[4]))#aqui ele salvara o canacelamento,ou seja ele mudara apena o elemento 3, o ativo, (conrtando com 0,1.2.3)
    print("Cancelado com sucesso!")
    menu_de_opcoes()

def valor_pagar():
    z=total()
    print("O valor a pagar é R$ %.2f "%(z[2]))
    sla=input("pressione Enter para voltar para o menu")
    if sla==sla:
        menu_de_opcoes()

def total(): #esta e um sub funcao onde retona o total do valor, tendo login
    var=login()
    variaveis=[var[0],var[2]] #as informacoes do nome e cpf estavam no login vou guardalas aqui, var[0]=cpf,var[2]=nome
    pedidos = {  # faco um dicionario onde guarda os o valores e nome dos pedidos  pelo chave codigo produto
        "1": [10.00, "X-SAlada"],
        "2": [10.00, 'X-Burguer'],
        "3": [7.50, 'Cachorro Quente'],
        "4": [8.00, 'Misto Quente'],
        "5": [5.50, 'Salada de Frutas'],
        "6": [4.50, 'Refrigerante'],
        "7": [6.25, 'Suco Natural']
    }
    cpf=var[0]
    if var[1]==1:
        lista=procura_linha_cpf(cpf) #chamo o modulo onde ele retorna a linha em formato de lista, onde o cpf estiver que foi enviado
        total=0
        hora=lista[4]
        for x,y,z in zip(lista[1],lista[2],lista[3]):# elemento x= codigo do produto, y quantidade do produto, z se ele esta ativo ou nao, 1=ativo,0=cancelado, no caso estou pegando caractere por caractere e guardando em seus correspondentes x,y,z
            if z=="1": #se o produto esta ativo somara no total
                total+=pedidos[x][0]*int(y)
        variaveis = [var[0], var[2],total,hora]  # as informacoes do nome e cpf estavam no login vou guardalas aqui, var[0]=cpf,var[2]=nome
        return variaveis

def extrato():
    variaveis=total() #recebera as variaveis aqui com o cpf e nome e o total
    cpf=variaveis[0] #organizo estas
    nome=variaveis[1]
    valor=variaveis[2]
    hora=variaveis[3]
    print("""
Nome: %s
CPF: %s
Total: R$ %.2f
Data: %s
Itens do Pedido:
"""%(nome,cpf,valor,hora))
    deco(cpf)

menu_de_opcoes()
