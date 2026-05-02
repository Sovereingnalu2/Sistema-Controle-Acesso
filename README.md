# Sistema de Controle de Acesso

## SOBRE O PROJETO
Este projeto é um sistema de controle de acesso com diferentes níveis de permissão (admin, gerente, usuário). Foi desenvolvido como parte dos meus estudos em Ciência da Computação para praticar conceitos de modelagem de dados, segurança e auditoria.

## FUNCIONALIDADES
- Login com autenticação (senhas com hash - não armazenadas em texto puro)
- 3 níveis de acesso: Admin, Gerente e Usuário comum
-  Usuários comuns só veem seus próprios dados
-  Gerentes veem dados de nível admin e gerente
-  Administradores têm acesso total
-  Log de auditoria registra todas as ações

## TECNOLOGIAS UTILIZADAS
- Python 3
- SQLite (banco de dados relacional)
- Hashlib (para segurança de senhas)

## ESTRUTURA DO PROJETO
- sistema-controle-acesso/
- cria_banco.py # Cria as tabelas do banco de dados
- cria_usuarios.py # Cadastra usuários iniciais
- login.py # Sistema de autenticação
- adiciona_dados.py # Adiciona dados protegidos
- consulta.py # Consulta dados com controle de acesso
- ver_logs.py # Visualiza logs de auditoria
- .gitignore # Arquivos ignorados pelo Git
- README.md # Este arquivo


## COMO EXECUTAR
1. Clone o repositório: `git clone https://github.com/seu-usuario/sistema-controle-acesso.git`
2. Entre na pasta: `cd sistema-controle-acesso`
3. Execute: `python cria_banco.py`
4. Execute: `python cria_usuarios.py`
5. Teste com os usuários:
   - ana@empresa.com / admin123 (acesso total)
   - carlos@empresa.com / gerente123 (acesso intermediário)
   - julia@empresa.com / usuario123 (acesso básico)

##  AUTORA
Stephanny Araújo - Estudante de Ciência da Computação

## STATUS DO PROJETP
Concluído - Disponível para portfólio e melhorias futuras
