import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config

class TestRemoveRole(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U1', 'RO0')
        self.assertEquals(result, "Incorrect User ID")

    def test2_InvalidRoleID(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO3')
        self.assertEquals(result, "Invalid Role ID")

    def test3_RoleNotExist(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO1')
        self.assertEquals(result, "There is no such role in the user account")

    def test4_removeRole(self):
        object = RoleBaseAccessControl()
        result = object.removeRole('U0', 'RO2')
        self.assertEquals(result, "Role has been removed from the User")
        object.assignRole('U0', 'RO2')

if __name__ == '__main__':
    unittest.main()