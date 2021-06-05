import unittest
from src.RBAC import RoleBaseAccessControl

class TestLoginUser(unittest.TestCase):
    def test1_loginUserExist(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('U0')
        self.assertEquals(result, "hi! you are logged in as U0, Admin")

    def test2_loginUserDoesntExist(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('U1')
        self.assertEquals(result, "User Doesn't Exist!!")

    def test3_loginUserIdEmpty(self):
        object = RoleBaseAccessControl()
        result = object.loginUser('')
        self.assertEquals(result, "User Doesn't Exist!!")

if __name__ == '__main__':
    unittest.main()