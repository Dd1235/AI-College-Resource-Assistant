import os


class Config:
    """Base configuration"""

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    ENV = "development"


class ProductionConfig(Config):
    """Production configuration"""

    DEBUG = False
    ENV = "production"
