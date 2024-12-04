from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

FILEPATH_IMPERIO = "dados.json"



@app.route('/', methods=['GET'])
def home():
    if os.path.exists(FILEPATH_IMPERIO):
        with open(FILEPATH_IMPERIO, "r") as f:
            data = json.load(f)
    listaImperiosHTML = """"""
    for i in data:
        nomeImperio = i #{'planets_name': ['err'], 'empire_name': '12e2w'}
        button ="""<a href="empire_detail?empire={}" >{}</a>""".format(nomeImperio, nomeImperio['empire_name'])
        listaImperiosHTML = listaImperiosHTML + button + "<br>"
    return render_template('index.php',listaImperios = listaImperiosHTML)


@app.route('/create_empire',)
def create_empire():
    return render_template('create_empire.html') 

@app.route('/submit_empire', methods=["POST"])
def submit_empire():
    # Obter dados do formulário
    data = request.form.to_dict()
    if 'planets_name' in data:
        data['planets_name'] = [""]
    if 'economia' in data:
        data['economia'] = [0, 0, 0]
    # Verificar se o arquivo já existe
    if os.path.exists(FILEPATH_IMPERIO):
        with open(FILEPATH_IMPERIO, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # Adicionar novos dados
    existing_data.append(data)

    # Salvar no arquivo JSON
    with open(FILEPATH_IMPERIO, "w") as f:
        json.dump(existing_data, f, indent=4)
    return home()


@app.route('/empire_detail', methods=['GET'])
def empire_detail():
    if request.args.get('empire'):
        infoEmpire = request.args.get('empire')
        infoEmpire = json.loads(infoEmpire.replace("'", '"'))
        empire_name = infoEmpire['empire_name']
    else:
        empire_name = request.args.get('empire_name')
    if os.path.exists(FILEPATH_IMPERIO):
        with open(FILEPATH_IMPERIO, "r") as f:
            data = json.load(f)

    for i in data:
        if i['empire_name'] == empire_name:
            data = i['planets_name']
            break
    listaPlanetasHTML = """"""
    for i in data:
        nomePlaneta = i 
        button ="""<a href="planet_detail?planet_name={}&empire_name={}">{}</a>""".format(nomePlaneta, empire_name, nomePlaneta)
        listaPlanetasHTML = listaPlanetasHTML + button + "<br>"
    
    return render_template('empire_detail.php', empire_name = empire_name, listaPlanetas = listaPlanetasHTML)



@app.route('/create_planet', methods=['GET'])
def create_planet():
    empire_name = request.args.get('empire_name')
    return render_template('create_planet.html', empire_name = empire_name) 



@app.route('/submit_planet', methods=["POST"])
def submit_planet():
    empire_name = request.args.get('empire_name')
    newPlanet = request.form.to_dict()['planet_name']

    if os.path.exists(FILEPATH_IMPERIO):
        with open(FILEPATH_IMPERIO, "r") as f:
            data = json.load(f)

    position = 0
    for i in data:
        if i['empire_name'] == empire_name:
            break
        position =position + 1

    planetList = data[position]['planets_name']
    planetList.append(newPlanet)
    print(planetList)

    with open(FILEPATH_IMPERIO, "w") as f:
        json.dump(data, f, indent=4)

    novo_arq_json = "{}.json".format(newPlanet)

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

    with open(novo_arq_json, 'w') as f:
        json.dump(infoPlaneta, f, indent=4) 

    destiny = """<a href="empire_detail?empire_name={}">RETORNAR</a>""".format(empire_name)

    return  render_template('landing.php', empire_name = empire_name, destiny = destiny) 



@app.route('/planet_detail', methods=['GET'])
def planet_detail():
    planet_name = request.args.get('planet_name')
    FILEPATH_PLANETA = "{}.json".format(planet_name)
    empire_name = request.args.get('empire_name')
    if os.path.exists(FILEPATH_IMPERIO):
        with open(FILEPATH_IMPERIO, "r") as f:
            data = json.load(f)
    for i in data:
        if i['empire_name'] == empire_name:
            for x in i:
                if x == planet_name:
                    data = x
                    break
    
    if os.path.exists(FILEPATH_PLANETA):
        with open(FILEPATH_PLANETA, "r") as f:
            data = json.load(f)
            print(data)

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




