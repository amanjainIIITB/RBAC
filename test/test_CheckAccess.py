import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config


class TestCheckAccess(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U1', 'Read', 'RE0')
        self.assertEquals(result, "Incorrect User ID")

    def test2_InvalidActionType(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Red', 'RO3')
        self.assertEquals(result, "Incorrect Action Type")

    def test3_InvalidResource(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Read', 'RO3')
        self.assertEquals(result, "Resource not Found")

    def test4_AccessAllowed(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Read', 'RE2')
        self.assertEquals(result, "You are allowed to access the given Resource")

    def test5_AccessDenied(self):
        object = RoleBaseAccessControl()
        object.createUser('sample')
        object.assignRole('U1', 'RO1')
        result = object.is_access_allowed('U0', 'Read', 'RE2')
        self.assertEquals(result, "You are allowed to access the given Resource")
        object.removeRole('U1', 'RO1')
        config['USER'].pop('U1')

if __name__ == '__main__':
    unittest.main()
