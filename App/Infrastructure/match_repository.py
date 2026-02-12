from database import get_connection

class MatchRepository:

    def criar_match(self, id_perdido, id_achado):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO Match (id_perdido, id_achado, status)
        VALUES (?, ?, ?)""",
        (id_perdido, id_achado, "PENDENTE"))
        
        conn.commit()
        conn.close()