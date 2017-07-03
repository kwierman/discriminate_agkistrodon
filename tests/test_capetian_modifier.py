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

    def test_model_builds(self):
      assert(self.model is not None)

    def test_shapes_are_correct(self):
      input_shape = self.model.inputs[0].shape
      output_shape = self.model.outputs[0].shape
      assert(input_shape[0].value == output_shape[0].value)
      assert(input_shape[1].value*10 == output_shape[1].value)
      assert(input_shape[2].value == output_shape[2].value)
      assert(input_shape[3].value == output_shape[3].value)
      assert(input_shape[4].value == output_shape[4].value)
