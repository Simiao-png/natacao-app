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


def buscar_treino_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT * FROM treinos
        WHERE id = %s
    """

    cursor.execute(sql, (id,))
    treino = cursor.fetchone()

    cursor.close()
    conexao.close()

    return treino


def atualizar_treino(
    id,
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
        UPDATE treinos
        SET
            data_treino = %s,
            titulo = %s,
            estilo = %s,
            tamanho_piscina = %s,
            voltas = %s,
            distancia_metros = %s,
            duracao_minutos = %s,
            pace = %s,
            observacoes = %s,
            equipamentos = %s
        WHERE id = %s
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
        equipamentos,
        id
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def excluir_treino_por_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM treinos
        WHERE id = %s
    """

    cursor.execute(sql, (id,))
    conexao.commit()

    cursor.close()
    conexao.close()