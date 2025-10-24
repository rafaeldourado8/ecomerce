from logging.config import fileConfig

# --- AJUSTE 1: Importar create_engine ---
from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

# --- AJUSTE 2: Adicionar o path do projeto ---
# Este bloco corrige o 'ModuleNotFoundError: No module named 'app.database''
import os
import sys

# Adiciona a pasta pai (backend/) ao caminho de importação do Python
# __file__ é o caminho para este arquivo (backend/alembic/env.py)
# os.path.dirname(__file__) é a pasta 'backend/alembic'
# os.path.join(..., '..') "sobe" um nível para 'backend'
# Assumindo que seu app está em /app, subimos um nível para /app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ---------------------------------------------------

# --- AJUSTE 3: Importar a Base, URL e Modelos ---
# Agora que o path está correto, podemos importar do seu app
from app.db import Base, DATABASE_URL

# Importamos os MÓDULOS que contêm os modelos.
# Isso garante que todas as tabelas sejam "conhecidas"
# pelo SQLAlchemy Base antes de gerarmos a migração.
from app.user import models
from app.products import models 
from app.cart import models
# ------------------------------------------------


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- AJUSTE 4: Configurar o target_metadata ---
# Aponta o Alembic para os metadados do seu Base
target_metadata = Base.metadata
# ------------------------------------------------


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    # --- AJUSTE 5: Usar a DATABASE_URL do app ---
    # Em vez de ler do alembic.ini, usamos a URL do app/database.py
    url = DATABASE_URL
    # ---------------------------------------------
    
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # --- AJUSTE 6: Conectar usando a config do app ---
    # Substituímos o 'engine_from_config' para usar
    # a mesma DATABASE_URL que sua aplicação usa,
    # que por sua vez vem do config.py e do Docker.
    connectable = create_engine(DATABASE_URL)
    # ----------------------------------------------------

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


