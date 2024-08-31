from django.test import TestCase
from .models import NodeManager

class NodeManagerTest(TestCase):
    def setUp(self):
        self.manager = NodeManager()

    def test_create_node(self):
        result = self.manager.create_node(
            name="Test Node",
            label="Test Label",
            attributes="{'key':'value'}",
            relations="{}",
            description="A test node",
            created_by="tester"
        )
        self.assertIsNotNone(result)

    def test_update_node(self):
        self.manager.create_node(
            name="Test Node",
            label="Test Label",
            attributes="{'key':'value'}",
            relations="{}",
            description="A test node",
            created_by="tester"
        )
        result = self.manager.update_node(
            name="Test Node",
            description="An updated test node",
            modified_by="tester"
        )
        self.assertEqual(result[0]['n']['description'], "An updated test node")

    def test_delete_node(self):
        self.manager.create_node(
            name="Test Node",
            label="Test Label",
            attributes="{'key':'value'}",
            relations="{}",
            description="A test node",
            created_by="tester"
        )
        self.manager.delete_node("Test Node")
        result = self.manager.update_node(name="Test Node")
        self.assertEqual(len(result), 0)  # Should return no results
