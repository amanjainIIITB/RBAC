import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config

class TestAssignRole(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U1', 'RO0')
        self.assertEquals(result, "Incorrect User ID")

    def test2_InvalidRoleID(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO3')
        self.assertEquals(result, "Invalid Role ID")

    def test3_RoleAlreadyAssigned(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO2')
        self.assertEquals(result, "Role has already been assigned to the User")

    def test4_AssignRole(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO1')
        self.assertEquals(result, "Role has been assigned to the User")
        object.removeRole('U0', 'RO1')

if __name__ == '__main__':
    unittest.main()