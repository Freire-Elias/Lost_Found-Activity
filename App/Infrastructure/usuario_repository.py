from App.Infrastructure.database import get_connection

class UsuarioRepository:
    def inserir(self, nome, telefone, senha):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Usuarios(nome, telefone, senha)
            VALUES (?, ?, ?)""", (nome, telefone, senha))

        conn.commit()
        conn.close()

    def buscar_telefone(self, telefone):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM Usuarios WHERE telefone = ?",
            (telefone,)
        )
        usuario = cursor.fetchone()

        return dict(usuario)