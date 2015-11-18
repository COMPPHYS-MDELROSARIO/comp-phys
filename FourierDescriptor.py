import argparse
from matplotlib.backends.backend_pdf import PdfPages
def extract_shape (im_file, blowup = 1.0, plot_image = False, plot_contour = False, plot_contour_pts = False):
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    import numpy as np
    from skimage import feature

    im = mpimg.imread(im_file)
    
    if len(im.shape) == 3:
        # Takes one of the RGB channels
        im = im[:, :, 0]
        
    plt.figure()
    plt.imshow(im, cmap = plt.cm.gray)
    plt.title('The Image')
    
    x1 = np.arange(im.shape[1])
    y1 = np.arange(im.shape[0])
    x2 = x1 * blowup
    y2 = y1 * blowup
    y2 = y2[::-1]
    
    X, Y = np.meshgrid(x2, y2)
    
    plt.figure()
    if plot_image != False:
        plt.show()
    plt.title('Contour')
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    print 'countour level', levels
    
    cs_paths = CS.collections[0].get_paths()
    
    print 'numer of contour path', len(cs_paths)
    
    for x in range(len(cs_paths)):
        p = cs_paths[x]
        v = p.vertices
        xray = v[:,0]
        yray = v[:,1]
        plt.figure(0)
        plt.plot(xray, yray)


    if plot_contour != False:
        plt.show()
    if plot_contour_pts:
        plt.figure()
        plt.scatter(xray, yray) 
        
    return xray, yray

def FD(x, y, plot_FD = False, y_lim = None):
    import numpy as np
    z = x +y*1j
    z = np.fft.fft(z)
    
    if plot_FD == True:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'b-')
        if y_lim == None:
            plt.ylim([-10,10])
        else:
            plt.ylim([-y_lim, y_lim])
        
    plt.show()
    return z

def filt_Fd(Z, n_keep, no_zeroth = True):
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
    z = FD(x, y)
    z_filt = filt_FD(Z, order)
    if norm:
        Z_filt = size_norm(Z_filt)
    x_rec, y_rec = recover_shape(Z_filt)
    filte = np.abs(Z_filt)
    
    return filte, x_rec, y_rec

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    
    x_rec = z_rec.real
    y_rec = z_rec.imag
    
    return x_rec, y_rec

def size_norm(Z):
    return Z/np.sqrt(np.abs(Z[1]) * np.abs(Z[-1]))

a, b = extract_shape('number1.png')
c, d = extract_shape('number2.png')
e, f = extract_shape('number6.png')

#pp = PdfPages('rec_numbers126.pdf')
#pp.savefig(a)
#pp.savefig((a,b))
#pp.savefig((c,d))
#pp.savefig((e,f))
#pp.close()

#Was unsure how to complete the argparse part
#parser = argparse.ArgumentParser(description = 'Switch Order')
#parser.add_argument('-order', action = 'store', nargs = N, type = int)
#args = parser.parse_args()