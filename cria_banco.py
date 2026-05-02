# cria_banco.py
import sqlite3
import hashlib

# Conecta ao banco (cria o arquivo 'sistema.db' automaticamente)
conexao = sqlite3.connect('sistema.db')
cursor = conexao.cursor()

# ===== TABELA 1: USUÁRIOS =====
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    perfil TEXT CHECK(perfil IN ('admin', 'gerente', 'usuario')) NOT NULL
)
''')

# ===== TABELA 2: DADOS SENSÍVEIS =====
cursor.execute('''
CREATE TABLE IF NOT EXISTS dados_sensiveis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    nivel_acesso TEXT CHECK(nivel_acesso IN ('admin', 'gerente', 'usuario')) NOT NULL,
    criado_por INTEGER,
    FOREIGN KEY(criado_por) REFERENCES usuarios(id)
)
''')

# ===== TABELA 3: LOGS (histórico de tudo) =====
cursor.execute('''
CREATE TABLE IF NOT EXISTS logs_acesso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    acao TEXT NOT NULL,
    tabela_afetada TEXT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
''')

print("✅ Tabelas criadas com sucesso!")

conexao.commit()
conexao.close()