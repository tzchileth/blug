import unittest
from app.models import User 

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password = 'anything')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'anything')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = 'anything')
		self.assertTrue(u.verify_password('anything'))
		self.assertFalse(u.verify_password('something'))

	def test_password_salts_are_random(self):
		u1 = User(password = 'anything')
		u2 = User(password = 'anything')
		self.assertTrue(u1.password_hash != u2.password_hash)

