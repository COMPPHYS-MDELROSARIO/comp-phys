from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.image as mpimg
from scipy.interpolate import interp2d
from scipy import stats
from sklearn import decomposition
from sklearn.datasets import load_digits
from sklearn import svm
from sklearn.datasets import load_digits
from sklearn import preprocessing as pre

def interpol_im(im, dim1 = 8, dim2 = 8, plot_new_im = False, cmap = 'binary', axis_off = False):
    LImgur = mpimg.imread(im)
    LImgur=LImgur[:,:,0]
    
    x = np.arange(LImgur.shape[1])
    y = np.arange(LImgur.shape[0])

    f2d = interp2d(x, y, LImgur)

    x_new = np.linspace(0, LImgur.shape[1], dim1)
    y_new = np.linspace(0, LImgur.shape[0], dim2)

    LImgur_new = f2d(x_new, y_new)
    
    if plot_new_im == True:
        plt.imshow(LImgur_new,cmap = cmap, interpolation = 'nearest')
        if axis_off == True:
            plt.axis('off')
        plt.grid('off')
        plt.title('Interpolated Image')
        #Shows the interpolated image
        plt.show()
    LImgur_flat = LImgur_new.flatten()
    
    return LImgur_flat

def pca_X(X, n_comp = 10):
    md_pca = PCA(n_comp, whiten = True)
    Xproj = md_pca.fit_transform(X)
    return md_pca, Xproj

def pca_svm_pred(imfile, md_pca, md_clf, dim1 = 45, dim2 = 60):
    im = mpimg.imread(imfile)
    flattened = interpol_im(imfile, dim1, dim2, plot_new_im = True)
    Xproj = md_pca.transform(flattened)
    pred = md_clf.predict(Xproj[0])
    return pred

def rescale_pixel(X, unseen, ind = 0):
    scaler = pre.MinMaxScaler(feature_range = (min(X[ind]), max(X[ind])))
    scaled_unseen = scaler.fit_transform(X[ind],unseen).astype(int)
    return scaled_unseen

def svm_train(X, y, gamma = 0.001, C = 100):
    clf = svm.SVC(kernel = "poly", gamma = gamma, C = C)
    md_clf = clf.fit(X, y)
    return md_clf

