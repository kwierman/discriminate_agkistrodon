# -*- coding: utf-8 -*-
""" Model definitions for `discriminate_agkistrodon`

TODO: repeat for Conv3DTranspose
"""

from keras.layers import Input
from keras.layers.convolutional import (MaxPooling3D, Conv3D,
                                        UpSampling3D)
from keras.models import Model

import logging


class capetian_modifier(Model):
  """ Capetian modifier is the protomodel for FCN using LArNet inspired
  modules with a fully convolutional backend.

  For this prototype, the FC backend was created using 3D upsampling.

  Though it's memory intensive, the ``Attributes`` include links to
  each of the network's layers.

  Usage:

  Instantiation of the network functions as follows:

  .. code-block:: python

    model = capetian_modifier()
    model.compile()

  """

  logger = logging.getLogger('capetian_modifier')
  """Logger for this class"""

  def __init__(self):

    self.logger.info("Assembling Model")
    self._input = Input(shape=(1, 3, 9600, 3600))
    """keras.layers.Input: keras style input layer"""

    conv1 = Conv3D(32, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block1_conv1')(self._input)
    """keras.layers.convolutional.Conv3D: First block convolution"""
    pool1 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block1_pool')(conv1)
    """keras.layers.convolutional.MaxPooling3D: First block pooling"""
    # Block 2
    conv2 = Conv3D(64, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block2_conv1')(pool1)
    """keras.layers.convolutional.Conv3D: Second block convolution"""
    pool2 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block2_pool')(conv2)
    """keras.layers.convolutional.MaxPooling3D: Second block pooling"""
    # Block 3
    conv3 = Conv3D(128, (3, 2, 2), strides=(3, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block3_conv1')(pool2)
    """keras.layers.convolutional.Conv3D: Third block convolution"""
    pool3 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block3_pool')(conv3)
    """keras.layers.convolutional.Conv3D: Third block convolution"""

    # Block 4
    conv4 = Conv3D(256, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block4_conv1')(pool3)
    """keras.layers.convolutional.Conv3D: Fourth block convolution"""
    pool4 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         name='block4_pool',
                         data_format='channels_first')(conv4)

    # Block 5
    conv5 = Conv3D(512, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(pool4)
    """keras.layers.convolutional.Conv3D: Fifth block convolution"""
    pool5 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2), name='block5_pool',
                         data_format='channels_first')(conv5)

    # Block 6, Ze Fully Convolution Bloch
    conv6 = Conv3D(1024, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(pool5)
    conv7 = Conv3D(10, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(conv6)
    up7 = UpSampling3D(size=(3, 9600 / 3, 3600),
                       data_format='channels_first')(conv7)
    """str: Docstring *after* attribute, with type specified."""

    super(capetian_modifier, self).__init__(self._input, up7)

  def compile(self):
    """Calls default compile

    """
    self.logger.info("Compiling Model")
    self.compile(loss='categorical_crossentropy', optimizer='sgd',
                 metrics=['accuracy'])
