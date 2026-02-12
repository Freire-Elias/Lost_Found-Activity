
from database import get_connection

class ItemRepository:
    def inserir(self, tipo, nome, descricao, categoria, local, data, id_usuario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Itens(tipo, nome, descricao, categoria, local, data, id_usuario)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (tipo, nome, descricao, categoria, local, data, id_usuario))

        id_item = cursor.lastrowid
        conn.commit()
        conn.close()

        return id_item


    def buscar_tipo(self, tipo):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Itens WHERE tipo = ?""",
        (tipo,))

        resultados = cursor.fetchall()
        conn.commit()
        conn.close()

        return [dict(row) for row in resultados]

    def buscar_id(self, id_item):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Itens WHERE id_item = ?""",
        (id_item,))
        item = cursor.fetchone()
        conn.close()
        return dict(item)