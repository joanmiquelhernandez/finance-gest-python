import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'tu_clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tu_basededatos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Otras configuraciones comunes

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    # Otras configuraciones específicas de desarrollo

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')  
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    # Otras configuraciones específicas de producción



config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}