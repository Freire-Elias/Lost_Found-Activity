import sqlite3

def get_connection():
    conn = sqlite3.connect("AchadosPerdidos.db")
    conn.row_factory = sqlite3.Row
    return conn


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Usuarios(
# id_usuario INTEGER PRIMARY KEY,
# nome TEXT NOT NULL,
# telefone VARCHAR(12),
# senha INTEGER NOT NULL
# )
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Itens(
# id_item INTEGER PRIMARY KEY,
# tipo TEXT NOT NULL,
# nome TEXT NOT NULL,
# descricao TEXT,
# categoria TEXT NOT NULL,
# local TEXT NOT NULL,
# data DATE NOT NULL,
# id_usuario INTEGER,
# FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario))
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Match(
# id_match INTEGER PRIMARY KEY,
# id_item_perdido INTEGER,
# id_item_achado INTEGER,
# status TEXT,
# FOREIGN KEY (id_item_perdido) REFERENCES Itens(id_item),
# FOREIGN KEY (id_item_achado) REFERENCES Itens(id_item))
# """)
# conn.commit()
