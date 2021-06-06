import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config
from src.CONSTANT_MESSAGE import message


class TestCheckAccess(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U1', 'Read', 'RE0')
        self.assertEquals(result, message["InvalidUser"])

    def test2_InvalidActionType(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Red', 'RO3')
        self.assertEquals(result, message["InvalidActionType"])

    def test3_InvalidResource(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Read', 'RO3')
        self.assertEquals(result, message["ResourceNotFound"])

    def test4_AccessAllowed(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Read', 'RE2')
        self.assertEquals(result, message["AccessAllowed"])

    def test5_AccessDenied(self):
        object = RoleBaseAccessControl()
        object.createUser('sample')
        object.assignRole('U1', 'RO1')
        result = object.is_access_allowed('U1', 'Read', 'RE2')
        self.assertEquals(result, message["AccessNotAllowed"])
        object.removeRole('U1', 'RO1')
        config['USER'].pop('U1')

if __name__ == '__main__':
    unittest.main()
