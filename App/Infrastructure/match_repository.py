from App.Infrastructure.database import get_connection

class MatchRepository:

    def criar_match(self, id_perdido, id_achado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Match (id_item_perdido, id_item_achado, status)
        VALUES (?, ?, ?)""",
        (id_perdido, id_achado, "PENDENTE"))
        
        conn.commit()
        conn.close()

    def listar_matchs(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.id_match,
                   i1.nome AS item_perdido,
                   i2.nome AS item_achado,
                   m.status
            FROM Match m
            JOIN Itens i1 ON m.id_item_perdido = i1.id_item
            JOIN Itens i2 ON m.id_item_achado = i2.id_item
        """)
        matchs = cursor.fetchall()
        return [dict(m) for m in matchs]

    def listar_match_id(self, id_match):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""SELECT id_item_perdido, id_item_achado FROM Match
                        WHERE id_match = ?""", (id_match,))
        ids_match = cursor.fetchone()
        conn.close()
        return dict(ids_match)


