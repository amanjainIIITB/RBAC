import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config
from src.CONSTANT_MESSAGE import message

class TestAssignRole(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U1', 'RO0')
        self.assertEquals(result, message["InvalidUser"])

    def test2_InvalidRoleID(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO3')
        self.assertEquals(result, message["InvalidRole"])

    def test3_RoleAlreadyAssigned(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO2')
        self.assertEquals(result, message["RoleAlreadyAssigned"])

    def test4_AssignRole(self):
        object = RoleBaseAccessControl()
        result = object.assignRole('U0', 'RO1')
        self.assertEquals(result, message["RoleAssigned"])
        object.removeRole('U0', 'RO1')

if __name__ == '__main__':
    unittest.main()