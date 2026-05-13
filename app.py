from flask import Flask, render_template, request, redirect
from modelos.treinos import cadastrar_treino

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/salvar', methods=['POST'])
def salvar():
    data_treino = request.form['data_treino']
    titulo = request.form['titulo']
    estilo = request.form['estilo']
    tamanho_piscina = float(request.form['tamanho_piscina'])
    voltas = int(request.form['voltas'])
    duracao_minutos = int(request.form['duracao_minutos'])
    observacoes = request.form['observacoes']

    equipamentos = request.form.getlist('equipamentos')
    equipamentos = ', '.join(equipamentos)

    distancia_metros = tamanho_piscina * voltas

    cadastrar_treino(
        data_treino,
        titulo,
        estilo,
        tamanho_piscina,
        voltas,
        distancia_metros,
        duracao_minutos,
        observacoes,
        equipamentos
    )

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)