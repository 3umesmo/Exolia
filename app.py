#inportando bibliotecas
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

#criando o app
app = Flask(__name__)

#indicando o arquivo json principal
FILEPATH_PRINCIPAL = "dados.json"


#função para pg principal (apenas mostra a pagina e os impérios salvos)
@app.route('/', methods=['GET'])
def home():
    #verifica se o arq. JSON indicado no FILEPATH_PRINCIPAL existe
    if os.path.exists(FILEPATH_PRINCIPAL): 
        with open(FILEPATH_PRINCIPAL, "r") as f:
            #caso exista, coloca toda info dentro da variavel 'data'
            data = json.load(f)
    #variavel que irá armazenar o código HTML com o link de cada império
    listaImperiosHTML = """"""
    #for que percorre cada objeto do 'data'
    for i in data:
        nomeImperio = i #{'planets_name': ['Terra'], 'empire_name': 'Romano'} --> exemplo
        #adiciona um botão(que na vdd é um link) com as especificações de cada império
        button ="""<a href="empire_detail?empire={}" >{}</a>""".format(nomeImperio, nomeImperio['empire_name'])
        #adiciona o 'botão' à listaImperiosHTML
        listaImperiosHTML = listaImperiosHTML + button + "<br>"
    #retorna o template 'index.php', junto com a variavel listaImperios
    return render_template('index.php',listaImperios = listaImperiosHTML)



#função para pg de criar imperio (apenas mostra a pagina)
@app.route('/create_empire',)
def create_empire():
    return render_template('create_empire.html') 



#função para adicionar novo império
@app.route('/submit_empire', methods=["POST"])
def submit_empire():
    # Obter dados do formulário
    data = request.form.to_dict()
    #verifica se o dado 'planets_name' está entre os dados obitidos no form, caso tenha, o transforma em uma array 
    if 'planets_name' in data:
        data['planets_name'] = [""]
    #verifica se o dado 'planets_name' está entre os dados obitidos no form, caso tenha, o transforma em uma array 
    if 'economia' in data:
        data['economia'] = [0, 0, 0]
    # Verificar se o arquivo já existe
    if os.path.exists(FILEPATH_PRINCIPAL):
        with open(FILEPATH_PRINCIPAL, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # Adicionar novos dados
    existing_data.append(data)

    # Salvar no arquivo JSON
    with open(FILEPATH_PRINCIPAL, "w") as f:
        json.dump(existing_data, f, indent=4)
    return home()



#função para pg de detalhe do império (apenas mostra a pagina, trazendo todos os planetas do imperio)
@app.route('/empire_detail', methods=['GET'])
def empire_detail():
    #verifica se existe a informação 'empire' na url 
    if request.args.get('empire'):
        #caso exista, a adiciona na var 'infoEmpire'
        infoEmpire = request.args.get('empire')
        #converte a info obtida em um obj JSON
        infoEmpire = json.loads(infoEmpire.replace("'", '"'))
        #adiciona o dado 'empire_name' do obj JSON à var 'empire_name'
        empire_name = infoEmpire['empire_name']
    else:
        #caso não exista a info 'empire', ele pega a 'empire_name' (isso ocorerá quando a função 'submit_planet()' for chamada, já que ela envia o user de volta a essa pg, mas com outras info)
        empire_name = request.args.get('empire_name')

        
    if os.path.exists(FILEPATH_PRINCIPAL):
        with open(FILEPATH_PRINCIPAL, "r") as f:
            data = json.load(f)

    #for que percorre cada objeto do 'data'
    for i in data:
        #caso ache um obj com o 'empire_name' igual ao informado:
        if i['empire_name'] == empire_name:
            #var 'data' recebe a lista de planetas que esse império tem
            data = i['planets_name']
            break
    listaPlanetasHTML = """"""
    for i in data:
        nomePlaneta = i 
        button ="""<a href="planet_detail?planet_name={}&empire_name={}">{}</a>""".format(nomePlaneta, empire_name, nomePlaneta)
        listaPlanetasHTML = listaPlanetasHTML + button + "<br>"
    
    return render_template('empire_detail.php', empire_name = empire_name, listaPlanetas = listaPlanetasHTML)


#função para pg de criar planeta (apenas mostra a pagina)
@app.route('/create_planet', methods=['GET'])
def create_planet():
    empire_name = request.args.get('empire_name')
    return render_template('create_planet.html', empire_name = empire_name) 


#função para adicionar novo planeta ao imperio
@app.route('/submit_planet', methods=["POST"])
def submit_planet():
    empire_name = request.args.get('empire_name')
    #recebe o nome do planeta dado no form
    newPlanet = request.form.to_dict()['planet_name']

    if os.path.exists(FILEPATH_PRINCIPAL):
        with open(FILEPATH_PRINCIPAL, "r") as f:
            data = json.load(f)

    #var que armazenará a posição do obj que tem o nome do império
    position = 0
    #for que percorre todo o 'data' até encontrar o império com o nome dado
    for i in data:
        if i['empire_name'] == empire_name:
            break
        position =position + 1

    #var que recebe como valor a lista de planetas do império
    planetList = data[position]['planets_name']
    #adiciona à lista o nome do novo  planeta
    planetList.append(newPlanet)

    with open(FILEPATH_PRINCIPAL, "w") as f:
        json.dump(data, f, indent=4)

    #var que cria o nome do novo arq JSON, exclusivo do planeta novo
    novo_arq_json = "{}.json".format(newPlanet)

    #cria o obj do planeta
    infoPlaneta = {
    "nome": {newPlanet},
    "habitacao":0,
    "populacao":0,
    "numConstrucoes":0,
    "numGeradores":0,
    "numFabricasSimples":0,
    "numArmazens":0,
    "manutencaoLocal":0,
    "manutencaoLocal":0,
    "ganhoLocal":0,
    "minerio":0,
    "alimento":0,
    "componentesSimples":0,
    "combustivel":0
    }   

    #cria o arq e salva o conteúdo nele
    with open(novo_arq_json, 'w') as f:
        json.dump(infoPlaneta, f, indent=4) 

    #cria um link de volta para a pg 'empire_detail.php', enviando o nome do império na info  'empire_name'(esse é o motivo daquele if-else estranho no 'empire_detail()')
    destiny = """<a href="empire_detail?empire_name={}">RETORNAR</a>""".format(empire_name)

    return  render_template('landing.php', empire_name = empire_name, destiny = destiny) 


#função para pg de planeta (apenas mostra a pagina, recursos e construções do planeta)
@app.route('/planet_detail', methods=['GET'])
def planet_detail():
    planet_name = request.args.get('planet_name')
    #indicando o arquivo json espeçifico do planeta
    FILEPATH_PLANETA = "{}.json".format(planet_name)
    empire_name = request.args.get('empire_name')
    if os.path.exists(FILEPATH_PRINCIPAL):
        with open(FILEPATH_PRINCIPAL, "r") as f:
            data = json.load(f)
    
    if os.path.exists(FILEPATH_PLANETA):
        with open(FILEPATH_PLANETA, "r") as f:
            data = json.load(f)
            print(data)

    #cria variaveis q serão exportadas para a url
    habitacao = data['habitacao']
    populacao = data['populacao']
    numConstrucoes = data['numConstrucoes']
    numFazendas = data['numFazendas']
    numMinas = data['numMinas']
    numGeradores = data['numGeradores']
    numFabricasSimples = data['numFabricasSimples']
    numArmazens = data['numArmazens']
    numMinerio = data['minerio']
    numAlimento = data['alimento']
    numComponentesSimples = data['componentesSimples']
    numCombustivel = data['combustivel']
    


    return render_template('planet_detail.html', empire_name=empire_name,planet_name=planet_name,habitacao=habitacao,populacao=populacao,
                           numConstrucoes=numConstrucoes,numFazendas=numFazendas,numMinas=numMinas,numGeradores=numGeradores,
                           numFabricasSimples=numFabricasSimples,numArmazens=numArmazens,numMinerio=numMinerio,numAlimento=numAlimento,
                           numComponentesSimples=numComponentesSimples,numCombustivel=numCombustivel)




if __name__ == '__main__':
    app.run(debug=True)




