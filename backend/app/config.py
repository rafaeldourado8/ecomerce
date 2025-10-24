import os

APP_ENV = os.getenv('APP_ENV', 'devlopment')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecomerce')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecomerce_test')