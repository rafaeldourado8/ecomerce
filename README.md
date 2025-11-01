
<h1 align="center">🛍️ EcommerceApp API</h1>

<p align="center">
  <strong>API RESTful para um sistema de e-commerce, construída com Python, FastAPI, Docker, SQLAlchemy e PostgreSQL.</strong><br>
  <em>Projeto de portfólio focado em boas práticas e arquitetura escalável.</em>
</p>

---

## 🧱 Tecnologias Utilizadas

| Tecnologia | Descrição |
|-------------|------------|
| 🐍 **Python 3.10** | Linguagem principal do projeto |
| ⚡ **FastAPI** | Framework web de alta performance |
| 🧠 **SQLAlchemy** | ORM para modelagem de banco de dados |
| 🐘 **PostgreSQL** | Banco de dados relacional |
| 🔁 **Alembic** | Gerenciamento de migrações |
| 🐳 **Docker** | Containerização e ambiente consistente |

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
</p>

---

## ⚙️ Status do Projeto

🟡 **Em desenvolvimento**  
A arquitetura base (API + Banco de Dados + Docker) já está configurada.  
Os endpoints CRUD principais e as **rotas de autenticação** já estão implementados e documentados via Swagger UI (`/docs`).

---

## 🧩 Funcionalidades Implementadas — v1.0

### 👤 **Usuários**
- `GET /users/` → Listar todos os usuários  
- `POST /users/` → Criar um novo usuário  
- `GET /users/{user_id}` → Buscar usuário por ID  
- `DELETE /users/{user_id}` → Deletar usuário  

### 🔐 **Autenticação**
- `POST /auth/signup` → Registrar novo usuário  
- `POST /auth/login` → Fazer login e obter token JWT  
- `GET /auth/me` → Obter informações do usuário autenticado  

### 📦 **Produtos**
- `GET /products/` → Listar todos os produtos  
- `POST /products/` → Criar novo produto  
- `GET /products/{product_id}` → Buscar produto por ID  
- `PUT /products/{product_id}` → Atualizar produto  
- `DELETE /products/{product_id}` → Deletar produto  

### 🏷️ **Categorias**
- `GET /categories/` → Listar todas as categorias  
- `POST /categories/` → Criar nova categoria  
- `GET /categories/{category_id}` → Buscar categoria por ID  
- `PUT /categories/{category_id}` → Atualizar categoria  
- `DELETE /categories/{category_id}` → Deletar categoria  

---

## 🧭 Próximos Passos (Roadmap)

- [ ] 🔗 **Relacionamentos Avançados** — Refinar vínculos entre entidades  
- [ ] 🧾 **Testes Automatizados** — Implementar testes unitários e de integração  

---

## ⚡ Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/rafaeldourado8/ecommerceapp.git
cd ecommerceapp

# Suba os containers
docker-compose up -d

# Acesse a documentação Swagger
http://localhost:8000/docs
```

<img width="654" height="767" alt="image" src="https://github.com/user-attachments/assets/abf4f639-a17b-4a92-ba78-0da96b8c4f47" />



---

## 👨‍💻 Autor

**Rafael Dourado**  
Desenvolvedor Back-end Python  

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rafaeldourado8/)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rafael-dourado-dev/)

---

<p align="center">
  <em>“Construído com 💙 e FastAPI para impulsionar o futuro do comércio digital.”</em>
</p>
