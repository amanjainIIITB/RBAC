import unittest
from src.RBAC import RoleBaseAccessControl
from src.CONSTANT_MESSAGE import message

class TestRemoveRole(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U1', 'RO0')
        self.assertEquals(result, message["InvalidUser"])

    def test2_InvalidRoleID(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO3')
        self.assertEquals(result, message["InvalidRole"])

    def test3_RoleNotExist(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO1')
        self.assertEquals(result, message["RoleNotFoundInUserAccount"])

    def test4_removeRole(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO2')
        self.assertEquals(result, message["RoleRemoved"])
        object.assignRole('U0', 'RO2')

if __name__ == '__main__':
    unittest.main()