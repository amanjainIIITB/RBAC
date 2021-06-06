import unittest
from src.RBAC import RoleBaseAccessControl
from src.CONSTANT_MESSAGE import message

class TestLoginUser(unittest.TestCase):
    def test1_loginUserExist(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('U0')
        self.assertEquals(result, message["UserExist"]+"U0, Admin")

    def test2_loginUserNotExist(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('U1')
        self.assertEquals(result, message["UserNotExist"])

    def test3_loginUserIdEmpty(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('')
        self.assertEquals(result, message["UserNotExist"])

if __name__ == '__main__':
    unittest.main()