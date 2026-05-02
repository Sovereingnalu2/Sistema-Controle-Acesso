# corrige_banco.py
import sqlite3

conexao = sqlite3.connect('sistema.db')
cursor = conexao.cursor()

# ===== VER O QUE TEM NA TABELA =====
print("=== USUÁRIOS ATUAIS ===")
cursor.execute("SELECT id, nome, email, perfil FROM usuarios")
for usuario in cursor.fetchall():
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]} | Perfil: {usuario[3]}")

# ===== CORREÇÕES =====
print("\n=== APLICANDO CORREÇÕES ===")

# 1. Mudar nome do usuário com ID = 1 (Ana)
cursor.execute("UPDATE usuarios SET nome = 'Ana Souza' WHERE id = 1")
print("✅ Nome da Ana atualizado")

# 2. Mudar email do Carlos
cursor.execute("UPDATE usuarios SET email = 'carlos.novo@empresa.com' WHERE id = 2")
print("✅ Email do Carlos atualizado")

# 3. Deletar um usuário (se tiver algum errado)
# cursor.execute("DELETE FROM usuarios WHERE id = 5")
# print("✅ Usuário deletado")

# ===== VER O RESULTADO DEPOIS =====
print("\n=== USUÁRIOS DEPOIS DA CORREÇÃO ===")
cursor.execute("SELECT id, nome, email, perfil FROM usuarios")
for usuario in cursor.fetchall():
    print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]} | Perfil: {usuario[3]}")

conexao.commit()
conexao.close()