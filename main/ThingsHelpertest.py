from main.ThingsHelper import ThingsActions
import unittest
from ThingsHelper import ThingsModel

class ThingsModelTest(unittest.TestCase):

    def testModelSize(self):
        to_test = ThingsModel().get_model()
        self.assertIsInstance(to_test, dict)
        self.assertEqual(len(to_test.keys()),10,"model is incorrect correct size")

    def testGetAction(self):
        to_test = ThingsModel()
        self.assertEqual(to_test.get_action('paragraph').name, ThingsActions.note.name)
        self.assertEqual(to_test.get_action('heading_1').name, ThingsActions.header.name)
        self.assertEqual(to_test.get_action('bulleted_list_item').name, ThingsActions.item.name)
        self.assertEqual(to_test.get_action('toggle').name, ThingsActions.children.name)
        self.assertEqual(to_test.get_action('child_page').name, ThingsActions.none.name)