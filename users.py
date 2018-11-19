import uuid
from datetime import datetime

class User():
	users = []

	def register_user(self, name, role, password, confirm):
		self.name = name
		self.role = role
		self.password = password
		self.confirm = confirm

		if any(user_input == "" for user_input in (name, role, password, confirm)):
			return {"message" : "fields cannot be empty"}

		if not isinstance(name,str) or not isinstance(role,str):
			return "Input cann only be strings"

		if password == confirm: 

			new_user = {
				"userID" : str(uuid.uuid4().int),
				"name" : name,
				"role" : role,
				"password" : password,
				"logged_in": "False",
				"last_login": str(datetime.utcnow())
			}

			User.users.append(new_user)
			
			return User.users

		return "Your password does not match"
	
	def login(self, name, password):
		self.name = name
		self.password = password
		my_token = False

		count = 0

		while(count<len(User.users)):
			if User.users[count]['name'] == str(name):
				if User.users[count]['password'] ==  str(password):
					my_token = str(uuid.uuid4().int)
					User.users[count]['logged_in'] = my_token
					User.users[count]["last_login"] = str(datetime.utcnow())
					return my_token

			count = count + 1

		return "Invalid credentials"
			
	
	def logout(self, name):
		self.name = name

		count = 0

		while(count<len(User.users)):
			if User.users[count]['name'] == str(name):
				if User.users[count]['logged_in'] == "False":
					return {"message":"You are not logged in!!"}
				User.users[count]['logged_in'] = "False"
				return {"message":"Successfully Logged out!!"}

			count = count + 1

		return "User not in the system!!"