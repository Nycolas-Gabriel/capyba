# Projeto de Aplicativo de Cadastro e Login

Este projeto é um aplicativo web criado com o framework Django, que oferece funcionalidades de registro e login de usuários. O objetivo deste aplicativo é permitir que os usuários se cadastrem, façam login, visualizem itens e gerenciem seu perfil.

## Funcionalidades

- **Registro de Usuário**: Tela de registro com campos para nome, email, senha e foto de perfil.
- **Login de Usuário**: Tela de login com menu de navegação fácil que permite acesso a diferentes endpoints (login e cadastro).
- **Lista de Itens**: Após o login, os usuários são direcionados a uma tela que lista itens. Os usuários podem filtrar os itens por meio de uma barra de busca.
- **Perfil do Usuário**: Opção para visualizar o perfil do usuário, acessando o endpoint de perfil.
- **Alteração de Senha**: Funcionalidade para alterar a senha do usuário.
- **Logout**: Opção para sair da conta e retornar à tela de login.

## Estrutura do Projeto

- **Registro**: `register/`
  ![image](https://github.com/user-attachments/assets/20874d47-da3f-49b9-b125-4651f4821f40)

- **Login**: `login/`
  ![image](https://github.com/user-attachments/assets/ca0b1502-3778-41d6-be35-165c5ca2749f)

- **Lista de Itens**: `items/`
  ![image](https://github.com/user-attachments/assets/afab779b-fb03-4761-a10f-484405e1c140)

- **Perfil**: `profile/`
![image](https://github.com/user-attachments/assets/809364de-1a7f-411b-b279-57ed67a26faa)

## Recursos Utilizados

- **Django**: Framework web utilizado para desenvolver a aplicação.
- **Django Forms**: Usados para criar e gerenciar formulários de entrada de dados nas telas de registro e alteração de senha.
- **Pytest**: Utilizado para fazer testes de funções.

## Requisitos do Sistema

- Python 3.10+
- Django 5.1.1
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/Nycolas-Gabriel/capyba
   cd capyba
   ```

2. Instale as dependências usando o Poetry:
   ```bash
   poetry install
   ```
   2. Crie um ambiente virtual e instale as dependências venv:
   ```bash
   python -m venv venv
    source venv/bin/activate  # Unix
    .\venv\Scripts\activate  # Windows
    pip install -r requirements.txt

   ```

3. Rode as migrações do banco de dados:
   ```bash
   poetry run python manage.py migrate
             ou
   python manage.py migrate
   ```

4. Colete os arquivos estáticos:
   ```bash
   poetry run python manage.py collectstatic

                  ou

   python manage.py 
   ```

## Executando o Projeto Localmente

Para rodar o projeto localmente com o servidor de desenvolvimento do Django, use:

```bash
poetry run python manage.py runserver
              ou
python manage.py runserver
```

## Tecnologias Utilizadas

- Django 5.1.1
- Python 3.10+
- Whitenoise para servir arquivos estáticos
- Waitress como servidor WSGI para produção
