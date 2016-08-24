import os
basedir = os.path.abspath(os.path.dirname(__file__))
app_secret_key = os.urandom(24)
class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or app_secret_key
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
	SQLALCHEMY_RECORD_QUERIES = True
	BLUG_MAIL_SUBJECT_PREFIX = '[Blug]'
	BLUG_MAIL_SENDER = 'Blug Admin <achilesolomon@gmail.com>'
	BLUG_ADMIN = os.environ.get('BLUG_ADMIN')
	BLUG_POSTS_PER_PAGE = 20
	BLUG_FOLLOWERS_PER_PAGE = 50
	BLUG_COMMENTS_PER_PAGE = 30
	BLUG_SLOW_DB_QUERY_TIME=0.5



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
	@classmethod
	def init_app(cls, app):
		Config.init_app(app)

		# email errors to the administrators
		import logging
		from logging.handlers import SMTPHandler
		credentials = None 
		secure = None
		if getattr (cls, 'MAIL_USERNAME', None) is not None:
			credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
			if getattr(cls, 'MAIL_USE_TLS', None):
				secure = ()
		mail_handler = SMTPHandler( mailhost=(cls.MAIL_SERVER,cls.MAIL_PORT), 
			fromaddr=cls.BLUG_MAIL_SENDER, 
			toaddrs=[cls.BLUG_ADMIN], subject=cls.BLUG_MAIL_SUBJECT_PREFIX + ' Application Error ',
			credentials=credentials,
			secure=secure)
		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}