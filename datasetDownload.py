import collections
import datetime
import fluidsynth
import glob
import numpy as np
import pathlib
import pandas as pd
import pretty_midi
import seaborn as sns
import tensorflow as tf

from IPython import display
from matplotlib import pyplot as plt
from typing import Optional

data_dir = pathlib.Path('data/maestro-v2.0.0')
# if not data_dir.exists():
#   tf.keras.utils.get_file(
#       'maestro-v2.0.0-midi.zip',
#       origin='https://storage.googleapis.com/magentadata/datasets/maestro/v2.0.0/maestro-v2.0.0-midi.zip',
#       extract=True,
#       cache_dir='.', cache_subdir='data',
#   )
filenames = glob.glob(str(data_dir/'**/*.mid*'))
print('Number of files:', len(filenames))