from flask import Flask, render_template, request, redirect
from modelos.treinos import cadastrar_treino, listar_treinos

app = Flask(__name__)


@app.route('/')
def home():

    treinos = listar_treinos()

    return render_template(
        'index.html',
        treinos=treinos
    )


@app.route('/salvar', methods=['POST'])
def salvar():

    data_treino = request.form['data_treino']
    titulo = request.form['titulo']
    estilo = request.form['estilo']

    tamanho_piscina = float(
        request.form['tamanho_piscina']
    )

    voltas = int(
        request.form['voltas']
    )

    duracao_minutos = int(
        request.form['duracao_minutos']
    )

    observacoes = request.form['observacoes']

    equipamentos = request.form.getlist(
        'equipamentos'
    )

    equipamentos = ', '.join(equipamentos)

    distancia_metros = tamanho_piscina * voltas

    pace_decimal = (
        duracao_minutos /
        (distancia_metros / 100)
    )

    pace_minutos = int(pace_decimal)

    pace_segundos = int(
        (pace_decimal - pace_minutos) * 60
    )

    pace = (
        f"{pace_minutos}:"
        f"{pace_segundos:02d}"
    )

    cadastrar_treino(
        data_treino,
        titulo,
        estilo,
        tamanho_piscina,
        voltas,
        distancia_metros,
        duracao_minutos,
        pace,
        observacoes,
        equipamentos
    )

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)