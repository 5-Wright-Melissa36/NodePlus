# test_nodeplus.py
"""
Tests for NodePlus module.
"""

import unittest
from nodeplus import NodePlus

class TestNodePlus(unittest.TestCase):
    """Test cases for NodePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodePlus()
        self.assertIsInstance(instance, NodePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
