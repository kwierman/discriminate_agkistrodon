import pytest
import sys
import unittest
import logging
from discriminate_agkistrodon import aerophilatelic_pichi


class TestAerophilatelicPichi(unittest.TestCase):
    """
      Intrinsic unit tests of the capetian modifier
      model.
    """

    def setUp(self):
        self.model = aerophilatelic_pichi.aerophilatelic_pichi()

    def tearDown(self):
        del self.model

    def test_model_builds(self):
      """
        This should fail before the assert in the event
        that the model does not build
      """
      assert(self.model is not None)

    def test_shapes_are_correct(self):
      """
        Given the expected input shapes,
        the output shapes should be the same, but with 10 times the amount of filters
        since we're adding in 1 filter per classification.
      """
      input_shape = self.model.inputs[0].shape
      output_shape = self.model.outputs[0].shape
      assert(input_shape[0].value == output_shape[0].value)
      assert(input_shape[1].value*10 == output_shape[1].value)
      assert(input_shape[2].value == output_shape[2].value)
      assert(input_shape[3].value == output_shape[3].value)
      assert(input_shape[4].value == output_shape[4].value)
