# adiciona_dados.py
import sqlite3
from login import fazer_login

def adicionar_dado(usuario_id, titulo, conteudo, nivel_acesso):
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    # Insere o dado
    cursor.execute('''
    INSERT INTO dados_sensiveis (titulo, conteudo, nivel_acesso, criado_por)
    VALUES (?, ?, ?, ?)
    ''', (titulo, conteudo, nivel_acesso, usuario_id))
    
    # Registra no LOG (importante!)
    cursor.execute('''
    INSERT INTO logs_acesso (usuario_id, acao, tabela_afetada)
    VALUES (?, ?, ?)
    ''', (usuario_id, f"Criou dado: {titulo}", "dados_sensiveis"))
    
    conexao.commit()
    conexao.close()
    print(f"✅ Dado '{titulo}' adicionado com sucesso!")

# Interface para o usuário
if __name__ == "__main__":
    print("=== ADICIONAR DADO PROTEGIDO ===\n")
    email = input("Seu email: ")
    senha = input("Sua senha: ")
    
    usuario = fazer_login(email, senha)
    
    if not usuario:
        print("❌ Login falhou!")
        exit()
    
    print(f"\nOlá {usuario['nome']} (perfil: {usuario['perfil']})")
    
    titulo = input("Título do dado: ")
    conteudo = input("Conteúdo: ")
    
    # Só admin pode criar dados de nível diferente do seu
    if usuario['perfil'] == 'admin':
        nivel = input("Nível de acesso (admin/gerente/usuario): ")
        while nivel not in ['admin', 'gerente', 'usuario']:
            nivel = input("Nível inválido. Escolha admin/gerente/usuario: ")
    else:
        nivel = usuario['perfil']
        print(f"Nível definido automaticamente: {nivel}")
    
    adicionar_dado(usuario['id'], titulo, conteudo, nivel)