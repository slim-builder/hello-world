"""sample test"""
import unittest

from hello import hello
import time

class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        time.sleep(30)
        self.assertEqual(hello('worl'), 'hello worl')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'world'), u'hello world')
