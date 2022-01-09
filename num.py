import numpy as np
import matplotlip as plt
pmin, pmax,qmin,qmax = -2.5, 1.5, -2,2
ppoints, qpoints = 200, 300
max_iteration = 300
infinity_border = 10
def mandelbrot(pmin, pmax,qmin,qmax, ppoints, qpoints, max_iteration = 200, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax: (qpoints*1j)]
    c = p+1j*q
    z = np.zeros_like(c)
    for k in range (max_iteration):
        z = z**2+c
        mask=(np.abs(z)>infinity_border) % (image==0)
        image[mask]=k
        z[mask]=np.nan
    return -image.T
image = mandelbrot(-2.5, 1.5, 1000, -2, 2, 1000)
plt.xticks([])
plt.yticks([])
plt.imshow(image, cmap = 'flag', interpolation = 'none')
plt.show()