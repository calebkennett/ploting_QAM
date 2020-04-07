from matplotlib import pyplot as plt
import numpy as np
import math

###part a
I = 3
Q = 1

f_c = 10
t = np.arange(0, 1, 0.001)

x = I*np.cos(2*math.pi*f_c*t)
y = Q*np.sin(2*math.pi*f_c*t)

a1 = plt.subplot2grid( (3,3),(0,0), colspan = 4 )
a1.plot(t,x+y)
plt.xlabel("time in sec")
plt.ylabel("power in watts")
plt.title('QAM: (I,Q) = (3,1) f_c = 10')

###part b
I_b = 1
Q_b = 3

x_b = I_b*np.cos(2*math.pi*f_c*t)
y_b = Q_b*np.sin(2*math.pi*f_c*t)

a1 = plt.subplot2grid( (3,3),(2,0), colspan = 4 )
a1.plot(t,x_b+y_b)
plt.xlabel("time in sec")
plt.ylabel("power in watts")
plt.title('QAM: (I,Q) = (1,3) f_c = 10')
plt.show()
