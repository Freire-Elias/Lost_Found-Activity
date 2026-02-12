from database import get_connection

class UsuarioRepository:
    def inserir(self, nome, telefone, senha):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Usuarios(nome, telefone, senha)
            VALUES (?, ?, ?)""", (nome, telefone, senha))

        conn.commit()
        conn.close()