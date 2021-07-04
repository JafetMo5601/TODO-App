import os


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    DEBUG = os.environ.get("DEBUG") == "True"


class ProductionConfig(Config):
    DEBUG = os.environ.get("DEBUG") == "True"


app_config = {"development": DevelopmentConfig, "production": ProductionConfig}

