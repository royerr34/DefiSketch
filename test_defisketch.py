# test_defisketch.py
"""
Tests for DefiSketch module.
"""

import unittest
from defisketch import DefiSketch

class TestDefiSketch(unittest.TestCase):
    """Test cases for DefiSketch class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiSketch()
        self.assertIsInstance(instance, DefiSketch)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiSketch()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
