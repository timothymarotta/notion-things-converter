import unittest
from ThingsHelper import ThingsModel

class ThingsModelTest(unittest.TestCase):

    def testModelSize(self):
        to_test = ThingsModel().get_model()
        self.assertIsInstance(to_test, dict)
        self.assertEqual(len(to_test.keys()),10,"model is incorrect correct size")