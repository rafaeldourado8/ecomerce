from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- INÍCIO DA CORREÇÃO ---
# Importa a Base (correto)
from app.db import Base
# Importa o módulo de config, NÃO o app.db
from app import config

# Importamos os MÓDULOS que contêm os modelos.
from app.user import models
from app.products import models 
from app.cart import models

# Cria uma URL SÍNCRONA apenas para o Alembic
# O Alembic precisa do driver psycopg2 para rodar
SYNC_DATABASE_URL = (
    f"postgresql+psycopg2://{config.DATABASE_USERNAME}:{config.DATABASE_PASSWORD}@"
    f"{config.DATABASE_HOST}/{config.DATABASE_NAME}"
)
# --- FIM DA CORREÇÃO ---


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if alembic_config.config_file_name is not None:
    fileConfig(alembic_config.config_file_name)

# Aponta o Alembic para os metadados do seu Base
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    """
    # Usa a URL síncrona
    url = SYNC_DATABASE_URL
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
    """
    # Usa a URL síncrona
    connectable = create_engine(SYNC_DATABASE_URL)

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