# API Comércio Eletrônico

API Restful para um sistema de e-commerce, construída com Python, FastAPI, Docker, SQLAlchemy e PostgreSQL. Este é um projeto de portfólio focado em boas práticas de desenvolvimento back-end.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Tecnologias Utilizadas

* **Python 3.10:** Linguagem principal do projeto.
* **FastAPI:** Framework web de alta performance para a construção da API.
* **SQLAlchemy (Asyncio):** ORM para interação assíncrona com o banco de dados.
* **PostgreSQL:** Banco de dados relacional.
* **Alembic:** Ferramenta para gerenciamento de migrações (migrations) do banco de dados.
* **Docker:** Utilizado para criar ambientes consistentes de desenvolvimento e produção (conteinerização).

## Status do Projeto

**Em desenvolvimento.** A arquitetura principal (API, Banco de Dados e Docker) está configurada. Os endpoints CRUD para Usuários, Produtos e Categorias, bem como o fluxo de Carrinho e Pedidos, estão implementados.

## Funcionalidades Implementadas (v1.0)

A API atualmente suporta as operações para as seguintes entidades:

### 👤 Usuários
* `GET /user/`: Listar todos os usuários
* `POST /user/`: Criar um novo usuário
* `GET /user/{user_id}`: Obter um usuário específico por ID
* `DELETE /user/{user_id}`: Deletar um usuário por ID

### 📦 Produtos
* `GET /products/`: Listar todos os produtos
* `POST /products/`: Criar um novo produto
* `GET /products/{product_id}`: Obter um produto específico por ID
* `PUT /products/{product_id}`: Atualizar um produto por ID
* `DELETE /products/{product_id}`: Deletar um produto por ID

### 🏷️ Categorias
* `GET /categories/`: Listar todas as categorias
* `POST /categories/`: Criar uma nova categoria
* `GET /categories/{category_id}`: Obter uma categoria específica por ID
* `PUT /categories/{category_id}`: Atualizar uma categoria por ID
* `DELETE /categories/{category_id}`: Deletar uma categoria por ID

### 🛒 Carrinho de Compras
* `POST /cart/add/{product_id}`: Adicionar um produto ao carrinho (por email de usuário)
* `GET /cart/{email}`: Visualizar o carrinho do usuário
* `DELETE /cart/{cart_item_id}`: Remover um item específico do carrinho

### 🧾 Pedidos (Orders)
* `POST /orders/`: Criar um pedido a partir do carrinho (por email de usuário)
* `GET /orders/`: Listar todos os pedidos de um usuário
* `GET /orders/{order_id}`: Obter detalhes de um pedido específico

## Próximos Passos (Roadmap)

As próximas funcionalidades planejadas para a API são:

* [ ] **Autenticação de Usuário:** Implementação de login e proteção de rotas com JWT (JSON Web Tokens).
* [ ] **Estoque (Qtd):** Implementar a lógica para diminuir a `qtd` do `Product` quando um `Order` for criado.
* [ ] **Testes:** Adicionar testes unitários e de integração (Pytest).
