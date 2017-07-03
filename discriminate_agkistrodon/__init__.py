from keras.layers import Input, Dropout, Dense, Flatten, concatenate
from keras.layers.convolutional import MaxPooling3D, Conv3D, Conv3DTranspose, UpSampling3D
from keras.models import Model

import logging


class capetian_modifier(Model):
  """
    My brother, where do you intend to go tonight?
    I heard that you missed your connecting flight,
    To the Blue Ridge Mountains, over near Tennessee
  """
  logger = logging.getLogger('capetian_modifier')

  def __init__(self):
    """
    You're ever welcome with me any time you like,
    Let's drive to the country side, 
    Leave behind some green-eyed look-a-likes,
    So no one gets worried, no
    """

    self.logger.info("Assembling Model")
    self._input = Input(shape=(1, 3, 9600, 3600))

    # Block 1
    conv1 = Conv3D(32, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block1_conv1')(self._input)
    pool1 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block1_pool')(conv1)

    # Block 2
    conv2 = Conv3D(64, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block2_conv1')(pool1)
    pool2 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block2_pool')(conv2)

    # Block 3
    conv3 = Conv3D(128, (3, 2, 2), strides=(3, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block3_conv1')(pool2)
    pool3 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2),
                         data_format='channels_first',
                         name='block3_pool')(conv3)

    # Block 4
    conv4 = Conv3D(256, (1, 2, 2), strides=(1, 2, 2),
                   activation='relu', padding='same',
                   data_format='channels_first',
                   name='block4_conv1')(pool3)
    pool4 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2), name='block4_pool',
                         data_format='channels_first')(conv4)

    # Block 5
    conv5 = Conv3D(512, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(pool4)
    pool5 = MaxPooling3D((1, 2, 2), strides=(1, 2, 2), name='block5_pool',
                         data_format='channels_first')(conv5)

    # Block 6, Ze Fully Convolution Bloch
    conv6 = Conv3D(1024, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(pool5)
    conv7 = Conv3D(10, (1, 2, 2), strides=(1, 2, 2), activation='relu',
                   padding='same', data_format='channels_first')(conv6)
    up7 = UpSampling3D(size=(3,9600/3, 3600),
                              data_format='channels_first')(conv7)



    super(capetian_modifier, self).__init__(self._input, up7)
    self.logger.info("Compiling Model")
    self.compile(loss='categorical_crossentropy', optimizer='sgd',
                 metrics=['accuracy'])

    def assemble(self):
      """
      In the quivering forest,
      Where the shivering dog rests,
      Our good grandfather
      Built a wooden nest
      And the river got frozen,
      And the hole got snowed in,
      And the yellow moon glowed bright
      """
      pass
