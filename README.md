# 🚗 Sistema de Estacionamento

Este projeto é uma aplicação web desenvolvida com **Python** e **Django**, com o objetivo de gerenciar o fluxo de veículos em um estacionamento. O sistema realiza o controle de entrada e saída dos veículos, calcula o tempo de permanência e o valor a ser pago automaticamente.

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Django
- SQLite (banco de dados padrão do Django)
- HTML (templates)
- CSS básico (opcional, para estilização simples)

## ✨ Funcionalidades

- Registro de entrada de veículos (com data e hora automática).
- Registro de saída com cálculo do tempo total estacionado.
- Cálculo automático do valor a ser pago com base no tempo.
- Listagem de veículos atualmente no estacionamento.
- Histórico de entradas e saídas (em desenvolvimento).

## ⚙️ Como Executar o Projeto Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/estacionamento.git
   cd estacionamento
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Instale as dependências necessárias:

bash
Copiar
Editar
pip install django
(Opcional) Gere o arquivo requirements.txt para manter o projeto organizado:

bash
Copiar
Editar
pip freeze > requirements.txt
Depois disso, qualquer pessoa pode instalar as dependências com:

bash
Copiar
Editar
pip install -r requirements.txt
Execute as migrações do banco:

bash
Copiar
Editar
python manage.py migrate
Inicie o servidor de desenvolvimento:

bash
Copiar
Editar
python manage.py runserver
Acesse o sistema no navegador:

cpp
Copiar
Editar
http://127.0.0.1:8000/