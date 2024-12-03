#importando funções
from functions import *

#Início Declarando variaveis iniciais

planeta = 0
listaPlanetas = ['P1', 'P2', 'P3']

#Créditos
#[SaldoTotal, ganho, manutenção]
economia = [0, [0, 0], [0, 0], [0, 0]]

#recursos
#[minerio, alimento, comp simples, pop, popEmpregada]
recursos = [[0, 0, 0, 6, 0], [0, 0, 0, 3, 0], [0, 0, 0, 3, 0]]

#calcula o nivel do superaficit
superaficit = [0, 0, 0]


#Gastos p/ construir estruturas
#[minério, crédito, componentes simples]
gastos = [[30, 30, 0], [15, 20, 0],[15, 20, 0], [40, 40, 0], [25, 30, 0], [15, 20, 0]]


#qtd emprego p/ estruturas
emprego = [0, 1, 1, 2, 2, 0]

#manutenção de estruturas p/ emprego
manutencao = [0, 1, 1, 0, 2, 2]


#qtd de estruturas planeta
#[empregados/estruturas]
qtdEstruturas = [[[recursos[planeta][3],8], [2,2], [1,1], [2,1], [1,1], [40,1]], [[recursos[planeta][3],2], [1,1], [0,1], [2,1], [0,0], [40,1]], [[recursos[planeta][3],2], [1,1], [0,1], [2,1], [0,0], [0,0]]]
#Fim Declarando variaveis iniciais


#menu
while True==True:
    
    #calcula manutenção e ganho
    i = 0    
    economia[planeta+1][0] = qtdEstruturas [planeta][3][0] * 6
    economia[planeta+1][1] = 0
    while i <= 5:
        if i == 5:
            economia[planeta+1][1] =  economia[planeta+1][1] + (manutencao[i] * qtdEstruturas [planeta][i][1])
        else:
            economia[planeta+1][1] =  economia[planeta+1][1] + (manutencao[i] * qtdEstruturas [planeta][i][0])
        i = i + 1

    #calcula pop empregada
    i = 0
    recursos[planeta][4] = 0
    while i <= 4:
        recursos[planeta][4] =  recursos[planeta][4] + qtdEstruturas[planeta][i][0]
        i = i + 1
    recursos[planeta][4] =  recursos[planeta][4] - qtdEstruturas[planeta][0][0]
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"Planeta atual: {listaPlanetas[planeta]}")
    print(f"Saldo total: {economia[0]}")
    print(f"Ganho: {economia[planeta+1][0]}")
    print(f"manutenção: {economia[planeta+1][1]}")
    print(f"balanço: {economia[planeta+1][0]-economia[planeta+1][1]}")
    print("-----------------------")
    print("RECURSOS:")
    print(f"espaço no armazém: {qtdEstruturas[planeta][5][0]}") if qtdEstruturas[planeta][5][0] > 0 else print("Armazém cheio!!")
    print(f"minérios: {recursos[planeta][0]}")
    print(f"alimento: {recursos[planeta][1]}")
    print(f"componentes simples: {recursos[planeta][2]}")
    print(f"população: {recursos[planeta][3]}({superaficit[planeta]}/25)")
    print(f"população empregada: {recursos[planeta][4]}")
    print(f"população desempregada: {recursos[planeta][3]-recursos[planeta][4]}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-")
    
    #qtd = quantidade de estruturas no planeta
    qtd = 0
    for i in qtdEstruturas:
        qtd = qtd + i[planeta][1]
    choice = input("Digite 'construir' para construir uma estrutura no planeta, 'gerenciar' para gerenciar sua pop e suas estruturas, 'trocar' para trocar de planeta, 'enviar' para enviar recursos para outro planeta ou 'terminar' para passar o turno: ")

    if choice == 'construir':
        if qtd < 20:
            estrutura = input("o que vc deseja construir: ")
            if estrutura == 'habitacao':
                construirEstrutura(0, economia, gastos, recursos, qtdEstruturas, planeta)

            if estrutura == 'fazenda':
                construirEstrutura(1, economia, gastos, recursos, qtdEstruturas, planeta)

            if estrutura == 'mina':
                construirEstrutura(2, economia, gastos, recursos, qtdEstruturas, planeta)

            if estrutura == 'gerador':
                construirEstrutura(3, economia, gastos, recursos, qtdEstruturas, planeta)

            if estrutura == 'fabricaSimples':
                construirEstrutura(4, economia, gastos, recursos, qtdEstruturas, planeta)

            if estrutura == 'armazem':
                construirEstrutura(5, economia, gastos, recursos, qtdEstruturas, planeta)
                qtdEstruturas[planeta][0] = qtdEstruturas[planeta][0] + 1
        else:
                print('Planeta já está com numero máximo de estruturas!')

    if choice == 'gerenciar':

        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"{qtd}/20 estruturas no mundo")
        print(f"{qtdEstruturas[planeta][0][0]}/{qtdEstruturas[planeta][0][1]} habitações")
        print(f"{qtdEstruturas[planeta][1][0]}/{qtdEstruturas[planeta][1][1]} fazendas")
        print(f"{qtdEstruturas[planeta][2][0]}/{qtdEstruturas[planeta][2][1]} minas")
        print(f"{qtdEstruturas[planeta][3][0]}/{qtdEstruturas[planeta][3][1]} geradores")
        print(f"{qtdEstruturas[planeta][4][0]}/{qtdEstruturas[planeta][4][1]} fabricas simples")
        print(f"{qtdEstruturas[planeta][5][0]}/{qtdEstruturas[planeta][5][1]} armazens")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")

        estrutura = input("Qual tido de estrutura deseja gerenciar: ")

        if estrutura == 'habitacao':
            if qtdEstruturas[planeta][0][1] > 0:
                acao = input('O que deseja fazer com essas estruturas: ')
                if acao == 'destruir':
                    qtdEstruturas[planeta][0][1] = qtdEstruturas[planeta][0][1] - 1
                    print('Estrutura destruida')
                else:
                    print('Habitação não emprega')
            else:
                print('Sem estruturas desse tipo no planeta')


        if estrutura == 'fazenda':
            gerenciarEstrutura(1, emprego, qtdEstruturas, recursos, planeta)

        
        if estrutura == 'mina':
            gerenciarEstrutura(2, emprego, qtdEstruturas, recursos, planeta)
        

        if estrutura == 'gerador':
            gerenciarEstrutura(3, emprego, qtdEstruturas, recursos, planeta)

        if estrutura == 'fabricaSimples':
            gerenciarEstrutura(4, emprego, qtdEstruturas, recursos, planeta)


        if estrutura == 'armazem':
            if qtdEstruturas[planeta][5][1] > 0:
                acao = input('O que deseja fazer com essas estruturas: ')
                if acao == 'destruir':
                    qtdEstruturas[planeta][0][1] = qtdEstruturas[planeta][0][1] - 1
                    print('Estrutura destruida')
                else:
                    print('armazem não emprega')
            else:
                print('Sem estruturas desse tipo no planeta')


    if choice == 'trocar':
        planetaNome = input("para qual planeta deseja ir: ")
        posicaoPlaneta = 0
        for i in listaPlanetas:
            if planetaNome == i:
                planeta = posicaoPlaneta
                print(f"viajando para o planeta {i}")
            posicaoPlaneta = posicaoPlaneta + 1


    if choice == 'enviar':
        recurso = input("Recurso a enviar: ")
        if recurso == 'minerio':
            enviarRecurso(0, recursos, planeta, listaPlanetas, qtdEstruturas)
        if recurso == 'alimento':
            enviarRecurso(1, recursos, planeta, listaPlanetas, qtdEstruturas)
        if recurso == 'componenteSimples':
            enviarRecurso(2, recursos, planeta, listaPlanetas, qtdEstruturas)

    #fazer todos os planetas funcionarem ao mesmo tempo
    if choice == 'terminar':
        #calcula o saldo total de cada turno
        i = 1
        while i <= len(listaPlanetas):
            economia[0] = economia[0] + (economia[i][0] - economia[i][1])
            i = i + 1

        #valida se tem armazem no planeta
        if qtdEstruturas[planeta][5][1] > 0 and qtdEstruturas[planeta][5][0] > 0:
            #calcula qtd de minério produzido
            recursos[planeta][0] = recursos[planeta][0] + (qtdEstruturas[planeta][2][0] * 5)
            qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] - (qtdEstruturas[planeta][2][0] * 5)
            #calcula qtd de comida produzida, tirando a parte consumida pela pop
            recursos[planeta][1] = (recursos[planeta][1] +qtdEstruturas[planeta][1][0] * 3) - recursos[planeta][3]
            qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] - ((qtdEstruturas[planeta][1][0] * 3) - recursos[planeta][3])
            #calcula a qtd de componente simples q é produzido
            producaoCompSimples = qtdEstruturas[planeta][4][0] * 1
            i = 1
            while i <= producaoCompSimples:
                #caso tenha mais de 3 minérios:
                if recursos[planeta][0] > 3:
                    #adiciona 1 comp. simples
                    recursos[planeta][2] = recursos[planeta][2] + 1
                    #retira 3 minérios
                    recursos[planeta][0] = recursos[planeta][0] - 3   
                    qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] + 2
                i = i + 1
        if qtdEstruturas[planeta][5][0] == 0 and qtdEstruturas[planeta][0][1] > qtdEstruturas[planeta][0][0]:
            superaficit[planeta] = superaficit[planeta] + (qtdEstruturas[planeta][1][0] * 3) - recursos[planeta][3]
 

        #caso o superaficit tenha alcançado 25, cria mais 1 de pop
        if superaficit[planeta] >= 25:
            recursos[planeta][3] = recursos[planeta][3] + 1
            superaficit[planeta] = 0
            qtdEstruturas[planeta][0][0]  = qtdEstruturas[planeta][0][0] + 1
        #caso tenha sobra de alimento e tenha habitação disponível, adiciona o escedente de alimento ao superaficit
        if recursos[planeta][1] > 0 and qtdEstruturas[planeta][0][1] > qtdEstruturas[planeta][0][0]:
            superaficit[planeta] = superaficit[planeta] + recursos[planeta][1]
            qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] + recursos[planeta][1]
            recursos[planeta][1] = 0

        
        #caso a pop produza menos comida do que consome, o alimento fica negativo
        if recursos[planeta][1] < 0:
            #elimina parte da pop até a produção de comida se equilibrar com a qtd de pop
            recursos[planeta][3] = recursos[planeta][3] + recursos[planeta][1]

            #nesse código o recurso [pop] e empregados na qtdEstruturas são variaveis diferentes, tendo que retirar a qtd de empregados equivalente a qtd de pop que "morreu"
            #fiz retirar os empregados da mina primeiro
            qtdEstruturas[planeta][2][0] = qtdEstruturas[planeta][2][0] + recursos[planeta][1]
            #caso mesmo tirando o equivalente do alimento que falta o alimento ainda esteja negativo(fazendo, a partir da formula acima, a qtd de empregados ser negativa):
            if qtdEstruturas[planeta][2][0] < 0 :
                #atualiza a qtd de alimento que falta
                recursos[planeta][1] = recursos[planeta][1] - qtdEstruturas[planeta][2][0]
                #zera os empregados da mina
                qtdEstruturas[planeta][2][0] = 0
                #retira agora os empregados do gerador
                qtdEstruturas[planeta][3][0] = qtdEstruturas[planeta][3][0] + recursos[planeta][1]
                if qtdEstruturas[planeta][3][0] < 0 :
                    recursos[planeta][1] = recursos[planeta][1] - qtdEstruturas[planeta][3][0]
                    qtdEstruturas[planeta][3][0] = 0
                    #retira agora os empregados da fábrica simples
                    qtdEstruturas[planeta][4][0] = qtdEstruturas[planeta][4][0] + recursos[planeta][1]
                    if qtdEstruturas[planeta][4][0] < 0 :
                        recursos[planeta][1] = recursos[planeta][1] - qtdEstruturas[planeta][4][0]
                        qtdEstruturas[planeta][4][0] = 0
            #zera a qtd de alimento, caso ainda n esteja zerada
            recursos[planeta][1] = 0