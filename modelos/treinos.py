from database.connection import conectar


def cadastrar_treino(
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
):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO treinos 
        (
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
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
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

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_treinos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT * FROM treinos
        ORDER BY data_treino DESC
    """

    cursor.execute(sql)
    treinos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return treinos