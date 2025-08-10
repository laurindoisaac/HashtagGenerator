# test_hashtaggenerator.py
"""
Tests for HashtagGenerator module.
"""

import unittest
from hashtaggenerator import HashtagGenerator

class TestHashtagGenerator(unittest.TestCase):
    """Test cases for HashtagGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashtagGenerator()
        self.assertIsInstance(instance, HashtagGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashtagGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
