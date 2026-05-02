# cria_usuarios.py
import sqlite3
import hashlib

def hash_senha(senha):
    """Transforma senha num código (hash) - não dá pra voltar atrás!"""
    return hashlib.sha256(senha.encode()).hexdigest()

# Conectar ao banco
conexao = sqlite3.connect('sistema.db')
cursor = conexao.cursor()

# Lista de usuários que vamos criar
usuarios = [
    ("Ana Admin", "ana@empresa.com", "admin123", "admin"),
    ("Carlos Gerente", "carlos@empresa.com", "gerente123", "gerente"),
    ("Julia Usuario", "julia@empresa.com", "usuario123", "usuario")
]

for nome, email, senha, perfil in usuarios:
    senha_hash = hash_senha(senha)
    try:
        cursor.execute('''
        INSERT INTO usuarios (nome, email, senha_hash, perfil)
        VALUES (?, ?, ?, ?)
        ''', (nome, email, senha_hash, perfil))
        print(f"✅ Usuário {nome} criado!")
    except sqlite3.IntegrityError:
        print(f"⚠️ Usuário {email} já existe, ignorando...")

conexao.commit()
conexao.close()

print("\n🎉 Todos os usuários cadastrados! Use no login:")
for nome, email, senha, _ in usuarios:
    print(f"   {email} / {senha}")