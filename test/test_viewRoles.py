import unittest
from src.RBAC import RoleBaseAccessControl

class TestViewRole(unittest.TestCase):

    def test1_viewRole(self):
        object = RoleBaseAccessControl()
        result = object.viewRoles()
        expected_output = [['RO0', 'Engineer'], ['RO1', 'Manager'], ['RO2', 'Admin']]
        self.assertEquals(result, expected_output)

if __name__ == '__main__':
    unittest.main()