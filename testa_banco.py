# testa_banco.py
import sqlite3
import os

# Cria o banco
conexao = sqlite3.connect('sistema.db')
conexao.close()

# Mostra onde o arquivo foi criado
caminho = os.path.abspath('sistema.db')
print(f"✅ Banco criado em: {caminho}")

# Lista os arquivos da pasta
print("\n📁 Arquivos na pasta atual:")
for arquivo in os.listdir('.'):
    print(f"   - {arquivo}")