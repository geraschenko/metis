# Copyright 2020 Verily Life Sciences LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd
from bsst import io as bsst_io
import numpy as np
import os

"""Library level constants for `villes`."""

LABELS_TO_DROP = ["under_60", "none", "other"] # Participant labels to not plot
FIRST_PLOT_DAY = None
SAVE_FILE_PATH = os.path.join(os.path.abspath(__file__).split('py')[0], 'act_villes')
FILE_OPEN_FN = bsst_io.open_fn

SUCCESS_DATES = slice(np.datetime64('2021-07-01'), np.datetime64('2021-10-01'))
HIST_BIN_WIDTH = 4 # time units
