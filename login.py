# login.py
import sqlite3
import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def fazer_login(email, senha):
    """Verifica se email e senha estão corretos"""
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    senha_hash = hash_senha(senha)
    
    cursor.execute('''
    SELECT id, nome, perfil FROM usuarios 
    WHERE email = ? AND senha_hash = ?
    ''', (email, senha_hash))
    
    usuario = cursor.fetchone()
    conexao.close()
    
    if usuario:
        return {"id": usuario[0], "nome": usuario[1], "perfil": usuario[2]}
    return None

# Teste rápido
if __name__ == "__main__":
    print("=== TESTE DE LOGIN ===\n")
    email = input("Email: ")
    senha = input("Senha: ")
    
    usuario = fazer_login(email, senha)
    if usuario:
        print(f"\n✅ Bem-vindo(a), {usuario['nome']}! (Perfil: {usuario['perfil']})")
    else:
        print("\n❌ Email ou senha incorretos!")