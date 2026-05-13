from flask import Flask
from modelos.treinos import cadastrar_treino

app = Flask(__name__)

@app.route('/')
def home():

    cadastrar_treino(
        '2026-05-13',
        'Treino leve',
        'Crawl',
        25.0,
        1200,
        50,
        'Treino teste'
    )

    return "Treino cadastrado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)