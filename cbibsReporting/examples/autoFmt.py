# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

# create an hourly date range
time = pd.date_range('01/01/2014', '4/01/2014', freq='H')
values = np.random.normal(0, 1, time.size).cumsum()

# This utility wrapper makes it convenient to create common layouts of subplots,
#   including the enclosing figure object, in a single call.
# subplots(nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True, 
#   subplot_kw=None, gridspec_kw=None, **fig_kw)
fig, ax = pyplot.subplots()

# ax can be either a single Axes object or an array of Axes objects if more 
#  than one subplot was created. The dimensions of the resulting array can 
#  be controlled with the squeeze keyword, see above.
ax.plot_date(time, values, marker='', linestyle='-')

fig.autofmt_xdate()
pyplot.show()