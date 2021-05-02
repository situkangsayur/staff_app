class Config(object):
    """
    Common configurations
    """
    
    # put any configuration here


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    LOG_MODE = "development"
    DEBUG = True
    MONGO = True

class TestingConfig(Config):
    """
    Development configurations
    """

    LOG_MODE = "testing"
    DEBUG = True
    MONGO = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    LOG_MODE = "production"
    DEBUG = False
    MONGO = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing' : TestingConfig
}
