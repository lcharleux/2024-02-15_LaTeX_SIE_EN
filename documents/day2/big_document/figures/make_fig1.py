import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/data.csv')

fig = plt.figure()
plt.plot(data['time'], data['position'])
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.savefig('fig1.png')