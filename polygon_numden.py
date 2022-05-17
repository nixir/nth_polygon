from fractions import Fraction
import math
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ims = []

n_seri = np.linspace(0.1,1,20)

for n in n_seri:

    frac_in = Fraction(n).limit_denominator(50)



    num = frac_in.numerator
    den = frac_in.denominator

    all_item = num*den

    if not all_item%2:
        continue

    theta = np.linspace(0, 2*np.pi, 100)

    radius = 1

    c_cos = radius*np.cos(theta)
    c_sin = radius*np.sin(theta)

    n_lin = np.linspace(1,all_item,all_item,endpoint = True)

    s_cos = radius*np.cos((n_lin/all_item) * (2*np.pi))
    s_sin = radius*np.sin((n_lin/all_item) * (2*np.pi))


    figure, axes = plt.subplots(1)

    axes.plot(c_cos, c_sin)
    axes.set_aspect(1)

    axes.scatter(s_cos,s_sin)

    if all_item%2:
        # k1 = n_lin[0:all_item:2]-1
        # k1 = np.insert(k1,len(k1),k1[0])
        # k2 = n_lin[1:all_item:2]-1

        # k = (np.concatenate([k1,k2])).astype('int64')

        k_tmp = np.arange(0,all_item)*math.floor(all_item/2)%all_item
        k = np.insert(k_tmp,len(k_tmp),k_tmp[0])

        axes.plot(s_cos[k],s_sin[k])
    else:
        s_cos = np.insert(s_cos,len(s_cos),s_cos[0])
        s_sin = np.insert(s_sin,len(s_sin),s_sin[0])
        axes.plot(s_cos,s_sin)

    title_str = str(num)+'/'+str(den)+' pi'

    plt.title(title_str)

    ims.append(plt)

    # ani = animation.ArtistAnimation(fig,ims)
    plt.show()

