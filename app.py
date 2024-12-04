from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados armazenados em memória (simulação)
users = {}
campaigns = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Usuário já existe!"
        users[username] = {'password': password, 'empires': []}
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return redirect(url_for('dashboard', username=username))
        return "Usuário ou senha inválidos!"
    return render_template('login.html')

@app.route('/<username>/dashboard')
def dashboard(username):
    if username not in users:
        return "Usuário não encontrado!"
    empires = users[username]['empires']
    return render_template('dashboard.html', username=username, empires=empires)

@app.route('/<username>/create_empire', methods=['GET', 'POST'])
def create_empire(username):
    if request.method == 'POST':
        empire_name = request.form['empire_name']
        new_empire = {
            'name': empire_name,
            'planets': []
        }
        users[username]['empires'].append(new_empire)
        return redirect(url_for('dashboard', username=username))
    return render_template('create_empire.html', username=username)

@app.route('/<username>/empire/<empire_name>')
def empire_details(username, empire_name):
    empire = next((e for e in users[username]['empires'] if e['name'] == empire_name), None)
    if not empire:
        return "Império não encontrado!"
    return render_template('empire.html', username=username, empire=empire)

@app.route('/<username>/empire/<empire_name>/add_planet', methods=['GET', 'POST'])
def add_planet(username, empire_name):
        print("Rota acessada")  # Confirma que a rota foi acessada
        empire = next((e for e in users[username]['empires'] if e['name'] == empire_name), None)
        if not empire:
            print("Império não encontrado!")
            return "Império não encontrado!"

        if request.method == 'POST':
            print("Dados enviados no formulário:", request.form)  # Verifica os dados do formulário
            planet_name = request.form.get('planet_name')
            if not planet_name:
                print("Nenhum nome de planeta foi fornecido")
                return "Por favor, forneça o nome do planeta."

            new_planet = {
                'name': planet_name,
                'details': {
                    'Habitação': '0/0',
                    'População': '0/0',
                    'Número de Construções': '0/0',
                    'Construções': [],
                    'Manutenção Planetária': '0 Créditos/Turno'
                }
            }
            empire['planets'].append(new_planet)
            print(f"Planeta {planet_name} adicionado ao império {empire_name}")
            return redirect(url_for('empire_details', username=username, empire_name=empire_name))

        return render_template('add_planet.html', username=username, empire_name=empire_name)

# Rota para exibir os detalhes de um planeta
@app.route('/<username>/empire/<empire_name>/planet/<planet_name>')
def planet_details(username, empire_name, planet_name):
    empire = next((e for e in users[username]['empires'] if e['name'] == empire_name), None)
    if not empire:
        return "Império não encontrado!"

    planet = next((p for p in empire['planets'] if p['name'] == planet_name), None)
    if not planet:
        return "Planeta não encontrado!"

    return render_template('planet_details.html', username=username, empire_name=empire_name, planet=planet)
    
@app.route('/<username>/empire/<empire_name>/planet/<planet_name>/manage_building/<building_name>', methods=['GET', 'POST'])
def manage_building(username, empire_name, planet_name, building_name):
    empire = next((e for e in users[username]['empires'] if e['name'] == empire_name), None)
    if not empire:
        return "Império não encontrado!"

    planet = next((p for p in empire['planets'] if p['name'] == planet_name), None)
    if not planet:
        return "Planeta não encontrado!"

    building = next((b for b in planet['details']['Construções'] if b['nome'] == building_name), None)
    if not building:
        return "Construção não encontrada!"

    if request.method == 'POST':
        # Atribuindo ou desalocando trabalhadores
        trabalhadores = int(request.form.get('trabalhadores', 0))
        if trabalhadores > building['max_empregos']:
            return f"Máximo de {building['max_empregos']} trabalhadores para esta construção."
        building['empregos_atual'] = trabalhadores

        # Atualizando produção
        if building['tipo'] == 'Fazenda':
            building['producao'] = trabalhadores * 3  # 3 de comida por trabalhador
        elif building['tipo'] == 'Mina':
            building['producao'] = trabalhadores * 5  # 5 minérios por trabalhador
        elif building['tipo'] == 'Gerador':
            building['producao'] = trabalhadores * 12  # 12 créditos por trabalhador

        # Consumo de comida
        comida_consumida = trabalhadores * 1  # Cada trabalhador consome 1 comida
        return redirect(url_for('planet_details', username=username, empire_name=empire_name, planet_name=planet_name))

    return render_template('manage_building.html', username=username, empire_name=empire_name, planet_name=planet_name, building=building)

@app.route('/<username>/empire/<empire_name>/planet/<planet_name>/add_building', methods=['GET', 'POST'])
def add_building(username, empire_name, planet_name):
    empire = next((e for e in users[username]['empires'] if e['name'] == empire_name), None)
    planet = next((p for p in empire['planets'] if p['name'] == planet_name), None)

    if request.method == 'POST':
        building_name = request.form.get('building_name')
        building_type = request.form.get('building_type')

        # Validação simples
        if not building_name or not building_type:
            return "Erro: Nome e tipo da construção são obrigatórios."

        # Criando a nova construção
        new_building = {
            'nome': building_name,
            'tipo': building_type,
            'max_empregos': 1,
            'empregos_atual': 0,
            'producao': 0,
            'manutencao': {'custo': 2, 'tipo': 'Créditos'}
        }

        # Adicionando a construção no planeta
        if 'Construções' not in planet['details']:
            planet['details']['Construções'] = []
        planet['details']['Construções'].append(new_building)

        return redirect(url_for('planet_details', username=username, empire_name=empire_name, planet_name=planet_name))

    return render_template('add_building.html', username=username, empire_name=empire_name, planet_name=planet_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
