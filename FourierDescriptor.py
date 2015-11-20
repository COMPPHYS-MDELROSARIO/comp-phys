import argparse
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from skimage import feature
import pdb

def extract_shape (im_file, blowup = 1.0, plot_img = False, plot_contour = False, plot_contour_pts = False):
 
    xray = []
    yray = []

    im = mpimg.imread(im_file)
    
    if len(im.shape) > 2:
        # Takes one of the RGB channels
        im = im[:, :, 0]
    if plot_img == True:
        plt.figure()
        plt.title('The Image')
        plt.imshow(im, cmap = plt.cm.gray)
        
    x1 = np.arange(im.shape[1])
    y1 = np.arange(im.shape[0])
    x2 = x1 * blowup
    y2 = y1 * blowup
    y2 = y2[::-1]
    
    X, Y = np.meshgrid(x2, y2)
    
    plt.figure()
    plt.title('Contour')
    
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    
    print 'countour level', levels
    
    cs_paths = CS.collections[0].get_paths()
    
    print 'number of contour path', len(cs_paths)
    
    for x in range(len(cs_paths)):
        p = cs_paths[x]
        v = p.vertices 
        xray = (v[:,0])
        yray = (v[:,1])
        plt.figure(0)
        plt.plot(xray[x], yray[x])
        plt.savefig("rec_numbers126.pdf")


    if plot_contour == False:
        plt.close()
    if plot_contour_pts:
        plt.figure(0)
        for y in range(len(xray)):
            plt.scatter(xray[x], yray[x]) 
        
    return xray, yray

def FD(x, y, plot_FD = False, y_lim = None):
    import numpy as np
    z = x + y * 1j
    z = np.fft.fft(z)
    
    if plot_FD == True:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(z.real, 'b-')
        plt.plot(z.imag, 'b-')
        if y_lim == None:
            plt.ylim([-10,10])
        else:
            plt.ylim([-y_lim,y_lim])
        
    return z

def filt_FD(Z, n_keep, no_zeroth = True):
    N = len(Z)
    n = np.arange(len(Z))
    print 'Nyquist index', N/2
    filt0 = n > 0 if no_zeroth else 1
    filt1 = filt0 * (n <= n_keep)
    filt2 = (n > ((N - 1) - n_keep))
    
    print 'Number of components from both sides:', filt1.sum(), filt2.sum()
    filt = filt1 + filt2
    
    return Z * filt

def get_FD_abs(x, y, order = 10, norm = True, no_zeroth = True):
    FD_mag = []
    yr = []
    xr = []
    for b in range(len(x)):
        z = FD(x[b], y[b])
        z_filt = filt_FD(z, order, no_zeroth = True, norm = True)
        if norm:
            z_filt = size_norm(z_filt)
        x_rec, y_rec = recover_shape(z_filt)
        xr.append(x_rec)
        yr.append(y.rec)
        filte = np.abs(z_filt[z_filt != 0])
        FD_mag.append(filte)
    
    return FD_mag, xr, yr

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    
    x_rec = z_rec.real
    y_rec = z_rec.imag
    
    return x_rec, y_rec

def size_norm(Z):
    return Z/np.sqrt(np.abs(Z[1]) * np.abs(Z[-1]))

norm=True
order = 10
no_zeroth = False

parser = argparse.ArgumentParser(description = 'checks for norm and zeroth')
parser.add_argument('-norm', dest='norm', action='store_false')
parser.add_argument('-no_zeroth', dest = 'no_zeroth', action='store_false')
parser.set_defaults(no_zeroth=True, norm=True)
args = parser.parse_args()

a, b = extract_shape('number1.png', blowup = 1.0, plot_img = False, plot_contour = False, plot_contour_pts = False)
c, d = extract_shape('number2.png', blowup = 1.0, plot_img = False, plot_contour = False, plot_contour_pts = False)
e, f = extract_shape('number6.png', blowup = 1.0, plot_img = False, plot_contour = False, plot_contour_pts = False)

#fd1, x_rec1, y_rec1 = get_FD_abs(a, b, order = order, norm = norm, no_zeroth=no_zeroth)
#fd2, x_rec2, y_rec2 = get_FD_abs(c, d, order = order, norm = norm, no_zeroth=no_zeroth)
#fd3, x_rec3, y_rec3 = get_FD_abs(e, f, order = order, norm = norm, no_zeroth=no_zeroth)

plt.figure()
plt.show()

