#função para criar nova estrutura
def construirEstrutura(construcaoTipo, economia, gastos, recursos, qtdEstruturas, planeta):
    #avalia se o jogador tem os minérios e o crédito necessário para construir a estrutura
    if economia[0] >= gastos[construcaoTipo][1] and recursos[planeta][0] >= gastos[construcaoTipo][0]:
        #caso tenha ira adicionar mais 1 ao valor da qtd de estruturas no qtdEstruturas
        qtdEstruturas[planeta][construcaoTipo][1] = qtdEstruturas[planeta][construcaoTipo][1] + 1
        print("estrutura construida com sucesso")
        #retira os recursos utilizados
        economia[0] = economia[0] - gastos[construcaoTipo][1]
        recursos[planeta][0] = recursos[planeta][0] - gastos[construcaoTipo][0]
        qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] + gastos[construcaoTipo][0] 
    else:
        print("estrutura não foi construida")

###########################

#função para gerenciar as estruturas
def gerenciarEstrutura(construcaoTipo, emprego, qtdEstruturas, recursos, planeta):
    #valida se existe pelomenos 1 estrutura dessa no planeta
    if qtdEstruturas[planeta][construcaoTipo][1] > 0:
        acao = input('O que deseja fazer com essas estruturas: ')
        #caso a ação escolhida seja destruir:
        if acao == 'destruir':
            #diminui em 1 a qtd de estrutura no qtdEstrutura
            qtdEstruturas[planeta][construcaoTipo][1] = qtdEstruturas[planeta][construcaoTipo][1] - 1
            print('Estrutura destruida')

        #caso a ação escolhida seja empregar:
        if acao == 'empregar':
            #valida se existem pessoas desempregadas
            if recursos[planeta][3] == recursos[planeta][4]:
                print("sem pessoas desempregadas!")
            else:
                #valida se o tipo de estrutura já está com todas as vagas de emprego preenchidas
                if qtdEstruturas[planeta][construcaoTipo][0] < qtdEstruturas[planeta][construcaoTipo][1] * emprego[construcaoTipo]:
                    #pede q qtd de pop que quer empregar
                    empregar = int(input('Quantos empregados deseja empregar: ')) 
                    #valida se a qtd entregue é menor ou igual a pop desempregada
                    if empregar <= (recursos[planeta][3]-recursos[planeta][4]):
                        #adiciona a qtd de empregados à qtd de empregados do qtdEstruturas
                        qtdEstruturas[planeta][construcaoTipo][0] = qtdEstruturas[planeta][construcaoTipo][0] + empregar
                        print("trabalhadores empregados")
                        #adiciona o valor dado à pop empregada
                        recursos[planeta][4] = recursos[planeta][4] + empregar
                    else:
                        print("população desempregada é menor que essa quantidade")
                        print(f"população desempregada: {recursos[planeta][3]-recursos[planeta][4]}")
                else:
                    print('Estrutura já está com a capacidade máxima!')
                    
        #caso a ação escolhida seja desempregar:
        if acao == 'desempregar':
            #valida se a estrutura está com empregados
            if qtdEstruturas[planeta][construcaoTipo][0] > 0:
                #pede q qtd de pop que quer desempregar
                desempregar = int(input('Quantos empregados deseja despedir: '))
                #valida se a qtd dada é menor ou igual a qtd de empregados
                if desempregar <= qtdEstruturas[planeta][construcaoTipo][0]:
                    #retira dos empregados
                    qtdEstruturas[planeta][construcaoTipo][0] = qtdEstruturas[planeta][construcaoTipo][0] - desempregar
                    #retira da pop empregada
                    recursos[planeta][4] = recursos[planeta][4] - desempregar
                    print("trabalhadores despedidos")
                else:
                    #caso a qtd dada seja maior que a qtd de empregados, ele irá retirar todos os empregados
                    recursos[planeta][4] = recursos[planeta][4] - qtdEstruturas[planeta][construcaoTipo][0]
                    qtdEstruturas[planeta][construcaoTipo][0] = 0
                    print("Todos trabalhadores despedidos")
            else:
                print('Estrutura sem empregados')
    else:
        print('Sem estruturas desse tipo no planeta')

###########################

#função para enviar recursos entre planetas
#Isso seria as rotas, mas no momento está muito "cru", apenas tirando a qtd de itens de um planeta e adicionando a msm qtd no outro
def enviarRecurso(recurso, recursos, planeta, listaPlanetas, qtdEstruturas):
    qtdRecurso = int(input(f"quantidade de {recurso}: "))
    #valida se o planeta atual tem esse recurso na qtd dada
    if qtdRecurso <= recursos[planeta][0]:
        planetaDestino = input("para qual planeta o recurso será enviado: ")
        posicaoPlaneta = 0
        #procura na lista de planetas o planeta de destino
        for i in listaPlanetas:
            #caso encontre o planeta e ele tenha espaço no armazem para a qtd de recursos:
            if planetaDestino == i and qtdEstruturas[posicaoPlaneta][5][0] >= qtdRecurso:
                choice = input(f"deseja enviar {qtdRecurso} {recurso} para o planeta {i}? s ou n: ")
                #'envia' os recursos
                if choice == 's':  
                    #retira a qtd de recursos do planeta de origem
                    recursos[planeta][0] = recursos[planeta][0] - qtdRecurso
                    #aumenta o armazem do planeta de origem na qtd de itens tirados
                    recursos[posicaoPlaneta][0] = recursos[posicaoPlaneta][0] + qtdRecurso
                    #adiciona a qtd de recursos do planeta de destino
                    qtdEstruturas[planeta][5][0] = qtdEstruturas[planeta][5][0] + qtdRecurso
                    #reduz o armazem do planeta de destino na qtd de itens adicionados
                    qtdEstruturas[posicaoPlaneta][5][0] = qtdEstruturas[posicaoPlaneta][5][0] - qtdRecurso
                    print ("recurso enviado!")
                break
            posicaoPlaneta = posicaoPlaneta + 1