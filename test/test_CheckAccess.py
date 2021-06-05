import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config

class TestAssignRole(unittest.TestCase):

    def test1_InvalidUserID(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U1', 'Read', 'RE0')
        self.assertEquals(result, "Incorrect User ID")

    def test2_InvalidActionType(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Red', 'RO3')
        self.assertEquals(result, "Invalid Role ID")

    def test3_InvalidResource(self):
        object = RoleBaseAccessControl()
        result = object.is_access_allowed('U0', 'Read', 'RO3')
        self.assertEquals(result, "Role has already been assigned to the User")

if __name__ == '__main__':
    unittest.main()