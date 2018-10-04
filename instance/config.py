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
    DATABASE_URL= os.getenv('DATABASE_TEST_URL')

class ProductionConfig(Config):
    pass


app_config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}