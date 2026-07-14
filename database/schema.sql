CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_usuario TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS receita (
    id_receita INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data_receita TEXT NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS despesa (
    id_despesa INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data_despesa TEXT NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);
