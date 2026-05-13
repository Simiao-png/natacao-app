from database.connection import conectar

def cadastrar_treino(data_treino, titulo, estilo, tamanho_piscina, distancia_metros, duracao_minutos, observacoes):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO treinos 
        (data_treino, titulo, estilo, tamanho_piscina, distancia_metros, duracao_minutos, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (data_treino, titulo, estilo, tamanho_piscina, distancia_metros, duracao_minutos, observacoes)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()