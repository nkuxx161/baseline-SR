import pandas as pd
import os

curve_name = '5_k7'

data = pd.read_csv(os.path.join('result', curve_name+'.csv'))
timestamp = data['timestamp']
value = data['value']
mag = data['mag']
isAnomaly = data['isAnomaly']

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 

plt.subplot(3, 1, 1)
plt.plot(timestamp, value)
plt.title('value')

plt.subplot(3, 1, 2)
plt.plot(timestamp, mag)
plt.title('mag')

plt.subplot(3, 1, 3)
plt.plot(timestamp, isAnomaly)
plt.title('isAnomaly')

plt.savefig(os.path.join('./images', 'SR_'+curve_name+'.png'))
plt.show()
plt.close()