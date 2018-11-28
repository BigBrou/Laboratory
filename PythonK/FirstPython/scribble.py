
#import tensorflow as tf
#hello = tf.constant('Hello, Tensorflow')
#sess = tf.Session()
#print(sess.run(hello))

'''
dic = {'aa':[1,2,3]}

print(dic['aa'][2])
print(dic.get('aa')[2])

import datetime
datetime.datetime.strptime('2016-01-02', '%Y-%m-%d')
'''
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(0)
uniform_data = np.random.rand(10, 12)
print(uniform_data)
sns.heatmap(uniform_data)
plt.show()
