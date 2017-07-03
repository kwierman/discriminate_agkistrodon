import pytest
import sys
import unittest
import logging
from discriminate_agkistrodon import capetian_modifier

class TestCapetian_Modifier(unittest.TestCase):

    def setUp(self):
        self.model = capetian_modifier()

    def tearDown(self):
        del self.model

    def test_000_something(self):
        print self.model
