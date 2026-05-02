# consulta.py
import sqlite3
from login import fazer_login

def consultar_dados(usuario_logado):
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    perfil = usuario_logado['perfil']
    usuario_id = usuario_logado['id']
    
    # REGRAS DE ACESSO - Cada perfil vê uma coisa diferente!
    if perfil == 'admin':
        # Admin vê TUDO
        cursor.execute('''
        SELECT d.id, d.titulo, d.conteudo, d.nivel_acesso, u.nome
        FROM dados_sensiveis d
        LEFT JOIN usuarios u ON d.criado_por = u.id
        ''')
    elif perfil == 'gerente':
        # Gerente vê dados admin E gerente (não vê dados de usuário comum)
        cursor.execute('''
        SELECT d.id, d.titulo, d.conteudo, d.nivel_acesso, u.nome
        FROM dados_sensiveis d
        LEFT JOIN usuarios u ON d.criado_por = u.id
        WHERE d.nivel_acesso IN ('admin', 'gerente')
        ''')
    else:  # usuario comum
        # Usuário comum só vê nível 'usuario'
        cursor.execute('''
        SELECT d.id, d.titulo, d.conteudo, d.nivel_acesso, u.nome
        FROM dados_sensiveis d
        LEFT JOIN usuarios u ON d.criado_por = u.id
        WHERE d.nivel_acesso = 'usuario'
        ''')
    
    dados = cursor.fetchall()
    
    # Registra a consulta no LOG
    cursor.execute('''
    INSERT INTO logs_acesso (usuario_id, acao, tabela_afetada)
    VALUES (?, ?, ?)
    ''', (usuario_id, f"Consultou dados (perfil: {perfil})", "dados_sensiveis"))
    conexao.commit()
    conexao.close()
    
    return dados

# Interface
if __name__ == "__main__":
    print("=== CONSULTAR DADOS ===\n")
    email = input("Email: ")
    senha = input("Senha: ")
    
    usuario = fazer_login(email, senha)
    
    if not usuario:
        print("❌ Login falhou!")
        exit()
    
    print(f"\n✅ Logado como: {usuario['nome']} (Perfil: {usuario['perfil']})")
    
    # Mostra a regra aplicada
    if usuario['perfil'] == 'admin':
        print("📢 Regra: Admin vê TODOS os dados\n")
    elif usuario['perfil'] == 'gerente':
        print("📢 Regra: Gerente vê dados de nível Admin e Gerente\n")
    else:
        print("📢 Regra: Usuário comum vê apenas dados de nível 'usuario'\n")
    
    dados = consultar_dados(usuario)
    
    if not dados:
        print("📭 Nenhum dado disponível para seu perfil.")
    else:
        print("📋 DADOS QUE VOCÊ PODE VER:\n")
        for dado in dados:
            print(f"ID: {dado[0]}")
            print(f"Título: {dado[1]}")
            print(f"Conteúdo: {dado[2]}")
            print(f"Nível necessário: {dado[3]}")
            print(f"Criado por: {dado[4]}")
            print("-" * 50) 