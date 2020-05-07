class Base():
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Base):
    DEBUG = True
    DEVELOPMENT = True
    DATABASE_URI = 'mysql+pymysql://root:213213@15@127.0.0.1:3306/ksridigital'

class TestingConfig(Base):
    DEBUG = False
    TESTING = True
    DATABASE_URI = 'mysql+pymysql://root:213213@15@127.0.0.1:3306/ksridigital'

class ProductionConfig(Base):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mysql+pymysql://root:213213@15@/ksridigital?unix_socket=/cloudsql/gcp-test-app-231526:asia-east2:samanish'