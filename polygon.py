import math
import numpy as np
import matplotlib.pyplot as plt

n = 7

theta = np.linspace(0, 2*np.pi, 100)

radius = 1

c_cos = radius*np.cos(theta)
c_sin = radius*np.sin(theta)

n_lin = np.linspace(1,n,n,endpoint = True)

s_cos = radius*np.cos((n_lin/n) * (2*np.pi))
s_sin = radius*np.sin((n_lin/n) * (2*np.pi))


figure, axes = plt.subplots(1)

axes.plot(c_cos, c_sin)
axes.set_aspect(1)

axes.scatter(s_cos,s_sin)

if n%2:
    k1 = n_lin[0:n:2]-1
    # k1 = np.insert(k1,len(k1),k1[0])
    k2 = n_lin[1:n:2]-1
    k = (np.concatenate([k1,k2])).astype('int64')
    k = np.insert(k,len(k),k[0])
    axes.plot(s_cos[k],s_sin[k])
else:
    s_cos = np.insert(s_cos,len(s_cos),s_cos[0])
    s_sin = np.insert(s_sin,len(s_sin),s_sin[0])
    axes.plot(s_cos,s_sin)

plt.title('angle')
plt.show()
