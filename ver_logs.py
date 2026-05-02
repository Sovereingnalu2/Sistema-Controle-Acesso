# ver_logs.py
import sqlite3

def ver_logs():
    conexao = sqlite3.connect('sistema.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
    SELECT l.data_hora, u.nome, l.acao, l.tabela_afetada
    FROM logs_acesso l
    LEFT JOIN usuarios u ON l.usuario_id = u.id
    ORDER BY l.data_hora DESC
    LIMIT 20
    ''')
    
    logs = cursor.fetchall()
    conexao.close()
    
    print("=== ÚLTIMOS 20 EVENTOS DO SISTEMA ===\n")
    if not logs:
        print("Nenhum log encontrado.")
    else:
        for log in logs:
            print(f"📅 {log[0]} | 👤 {log[1] or 'Sistema'}")
            print(f"   Ação: {log[2]} | Tabela: {log[3]}")
            print()

if __name__ == "__main__":
    ver_logs()