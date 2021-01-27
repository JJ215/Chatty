import sqlite3

conn = sqlite3.connect('Profiles/profiles.db')

c = conn.cursor()

user_check = False
class Decide:
	OVER = "OVER 16"
	UNDER = "UNDER 16"
class User:
	def __init__(self, name, lastname, age, username, password):
		self.name = name
		self.lastname = lastname
		self.age = age
		self.username = username
		self.password = password
		self.age_class = self.age_class()
		self.username_check= self.username_check()

	def age_class(self):
		if self.age > 16:
			return Decide.OVER
		elif self.age <= 15:
			return Decide.UNDER
	def username_check(self):
		if self.username.lower() == self.password.lower():
			user_check = True
		else:
			user_check = False

def create_user(name, lastname, age, username, password):
	user = User(name, lastname, age, username, password)

	age_class = user.age_class

	user.username_check

	
	c.execute("""INSERT INTO profiles (name, lastname, age, username, password, user_check, age_class) VALUES (?, ?, ?, ?, ?, ?, ?)"""
		, (name, lastname, age, username, password, user_check, age_class))

	conn.commit()

def Read():
	c.execute("""SELECT * FROM profiles""")
	data = c.fetchall()

	for i in data:
		print(i)

def check_input(username, password):
	c.execute("""SELECT * FROM profiles""")

	data = c.fetchall()
	for i in data:
		if len(i[3]) == 0 or len(i[4]) == 0:
			return "Password or Username can not be a length of 0"
		elif username == i[3] and password == i[4]:
			return True
		elif username == i[3] and password != i[4]:
			return "Password is incorect"
		elif username != i[3] and password == i[4]:
			return "Username is incorect"
		else:
			return "Username and password are not correct"

