import unittest
from src.RBAC import RoleBaseAccessControl
from src.config import config

class TestLoginUser(unittest.TestCase):

    def tearDown(self):
        config['USER'].pop('U1')

    def test1_createUser(self):
        object = RoleBaseAccessControl()
        result = object.createUser('sample')
        self.assertEquals(result['USER']['U1'], config['USER']['U1'])

if __name__ == '__main__':
    unittest.main()