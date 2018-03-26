import plotly
#plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

import numpy as np

x = np.random.random_integers(0,30,5)
data = [go.Histogram(x=x)]

plotly.offline.plot(data, filename='second histogram')


