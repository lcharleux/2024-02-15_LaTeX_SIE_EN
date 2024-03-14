import numpy as np
from math import pi
import pandas as pd

freq = 1. # Hz

t = np.linspace(0.,10., 1001) # TIME
x = np.sin(2. * pi * t) # POSITION
df = pd.DataFrame({'time': t, 'position': x})
df.to_csv('data.csv', index=False)
