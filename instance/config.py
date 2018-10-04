import os


class Config:
    SECRET_KEY = 'ASSSFFFGFFG%^$%##$%'
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=False

class TestingConfig(Config):
    DEBUG=True
    TESTING=True
    DATABASE_URL="dbname='fastfood_test' host='localhost' port='5432' user='postgres' password='pass123'"

class ProductionConfig(Config):
    pass


app_config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}