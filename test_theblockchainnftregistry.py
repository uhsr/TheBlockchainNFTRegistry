# test_theblockchainnftregistry.py
"""
Tests for TheBlockchainNFTRegistry module.
"""

import unittest
from theblockchainnftregistry import TheBlockchainNFTRegistry

class TestTheBlockchainNFTRegistry(unittest.TestCase):
    """Test cases for TheBlockchainNFTRegistry class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TheBlockchainNFTRegistry()
        self.assertIsInstance(instance, TheBlockchainNFTRegistry)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TheBlockchainNFTRegistry()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
