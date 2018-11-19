import unittest
from user import User

class TestUser(unittest.TestCase):
    """User tests class"""
   
    def test_user_registration(self):
         "tests if new user can register"
         self.user = User()
         result= self.user.register_user("muni","user","123","123")
         self.assertEqual(result,self.user.users)

    def test_empty_fileds(self):
         "tests if fileds are empty"
         self.user = User()
         result= self.user.register_user("muni","","123","123")
         self.assertEqual(result["message"],"fields cannot be empty")

    def test_invalid_input(self):
        "tests if input is invalid"
        self.user = User()
        result= self.user.register_user("muni",3,"123","123")
        self.assertEqual(result,"Input cann only be strings")

    def test_password_mismatch(self):
        "tests if password match"
        self.user = User()
        result= self.user.register_user("muni","user","234","123")
        self.assertEqual(result,"Your password does not match")


        


if __name__ == '__main__':
    unittest.main(verbosity=2)