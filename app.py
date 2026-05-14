from flask import Flask, render_template, request, redirect
from modelos.treinos import cadastrar_treino, listar_treinos, buscar_treino_por_id
import calendar
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    treinos = listar_treinos()
    return render_template('index.html', treinos=treinos)


@app.route('/calendario')
def calendario():
    hoje = date.today()

    ano = int(request.args.get('ano', hoje.year))
    mes = int(request.args.get('mes', hoje.month))

    treinos = listar_treinos()

    treinos_por_dia = {}

    for treino in treinos:
        data = treino['data_treino']

        if data.year == ano and data.month == mes:
            dia = data.day

            if dia not in treinos_por_dia:
                treinos_por_dia[dia] = []

            treinos_por_dia[dia].append(treino)

    calendario_mes = calendar.monthcalendar(ano, mes)

    return render_template(
        'calendario.html',
        calendario_mes=calendario_mes,
        treinos_por_dia=treinos_por_dia,
        ano=ano,
        mes=mes
    )


@app.route('/treino/<int:id>')
def detalhe_treino(id):
    treino = buscar_treino_por_id(id)

    return render_template(
        'detalhe_treino.html',
        treino=treino
    )


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

    pace_decimal = duracao_minutos / (distancia_metros / 100)

    pace_minutos = int(pace_decimal)
    pace_segundos = int((pace_decimal - pace_minutos) * 60)

    pace = f"{pace_minutos}:{pace_segundos:02d}"

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
    

@app.route('/calendario')
def calendario():

    treinos = listar_treinos()

    return render_template(
        'calendario.html',
        treinos=treinos
    )