import os
basedir = os.path.abspath(os.path.dirname(__file__))
app_secret_key = os.urandom(24)
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or app_secret_key
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
	BLUG_MAIL_SUBJECT_PREFIX = '[Blug]'
	BLUG_MAIL_SENDER = 'Blug Admin <achilesolomon@gmail.com>'
	BLUG_ADMIN = os.environ.get('BLUG_ADMIN')
	BLUG_POSTS_PER_PAGE = 20
	BLUG_FOLLOWERS_PER_PAGE = 50
	BLUG_COMMENTS_PER_PAGE = 30




	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	DEBUG = True 
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True 
	MAIL_USE_SSL = False
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}