import unittest

from bcam_script import welcomescript


class WelcomeScriptTestCase(unittest.TestCase):
    '''
    Unit Tests for module welcomescript
    '''

    def setUp(self):
        self.welcomescript_test_object = welcomescript()

    def test_welcomescript_response(self):
        self.assertEqual(self.welcomescript_test_object.status_code, 200)

    def test_welcomescript(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()