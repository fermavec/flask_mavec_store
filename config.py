class Config:
    SECRET_KEY = 'g8f6d9j5h7k3l1m2n4p6q9r7s5t8u6v1w2x'


class DevelopmentConfig(Config):
    DEBUG = True


config={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}