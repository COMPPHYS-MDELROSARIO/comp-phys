from skimage import transform,data,io
import matplotlib.pyplot as plt
from IPython import display
import time
import matplotlib.image as mpimg
from scipy.interpolate import interp2d
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import numpy as np
import string

def make_let_im(let_file, dim = 16, ylo = 70, yhi = 220, xlo = 10, xhi = 200, edge_pix = 148, plot_let = False):
    LImgur = mpimg.imread(let_file)
    LImgur=LImgur[:,:,0]
    print 'Original Images Shape: {:s}'.format(LImgur.shape)


    LImgur=LImgur [ylo:yhi,xlo:xhi]

    LImgur[0:150,edge_pix:]=1

    x = np.arange(LImgur.shape[1])
    y = np.arange(LImgur.shape[0])

    f2d = interp2d(x, y, LImgur)

    x_new = np.linspace(0, LImgur.shape[1], dim)
    y_new = np.linspace(0, LImgur.shape[0], dim)

    LImgur_new = f2d(x_new, y_new)
    
    print 'New Image Shape: {:s}'.format(LImgur.shape)
    plt.grid('off')
    plt.imshow(LImgur,cmap="gray")
    plt.title('Cropped Image')
    plt.show()
    if plot_let == True:
        print 'Interpolated Image Shape: {:s}'.format(LImgur_new.shape)
        plt.imshow(LImgur_new,cmap="gray")
        plt.grid('off')
        plt.title('Interpolated Image')
        #Shows the interpolated image
        #plt.show()
    
    #This is the mean of the array subtracted from the array of the cropped image
    LImgur_final = LImgur_new - np.mean(LImgur_new)
    LImgur_flat = LImgur_new.flatten()
    #Uncomment the following line to print out the array
    #print LImgur_final = LImgur_new - np.mean(LImgur_new)
    
    return LImgur_new, LImgur_flat

def alphabet_pca(X, n_comp = 10):
    pca = PCA(n_comp)
    Xproj = pca.fit_transform(X)
    pca_comps = pca.components_
    return pca, Xproj, pca_comps

def show_pca(Xproj, pca_comps, dim = 16, let_idx = 0):
    n_comp = pca_comps.shape[0]
    f, axes = plt.subplots(1, n_comp, figsize = (10, 2), subplot_kw=dict(xticks=[], yticks=[]))
    dig_im = np.zeros((dim, dim))
    coeffs = Xproj[let_idx]
    plt.title('Eigenimages')

    for i in range(n_comp):
        axes[i].imshow(pca_comps[i].reshape((dim, dim)), cmap='binary')
        
    for i in range(n_comp):
        dig_im += coeffs[i]*pca_comps[i].reshape((dim, dim))

    fig, ax = plt.subplots(1, 1, figsize = (2, 2))
    ax.imshow(dig_im, cmap='binary')
    plt.title('PCA Image')
    # To turn off grid (under seaborn, the default for grid is on.)
    ax.grid(False)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    import doctest
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-let_idx', type = int)
    parser.add_argument('-n_comp', type = int)
    args = parser.parse_args()
    let_idx = args.let_idx
    n_comp = args.n_comp
    alph = string.ascii_uppercase
    flattened = []
    #This for loop prints out the cropped image of each letter and adjusts edge_pix for each        letter accordingly
    for letters in alph:
        if letters == 'A':
            edge = 138
        elif letters == 'B':
            edge = 130
        elif letters == 'C':
            edge = 129
        elif letters == 'D':
            edge = 140
        elif letters == 'E':
            edge = 120
        elif letters == 'F':
            edge = 113
        elif letters == 'G':
            edge = 148
        elif letters == 'H':
            edge = 147
        elif letters == 'I':
            edge = 130
        elif letters == 'J':
            edge = 85
        elif letters == 'K':
            edge = 126
        elif letters == 'L':
            edge = 106
        elif letters == 'M':
            edge = 160
        elif letters == 'N':
            edge = 150
        elif letters == 'O':
            edge = 155
        elif letters == 'P':
            edge = 125
        elif letters == 'Q':
            edge = 160
        elif letters == 'R':
            edge = 130
        elif letters == 'S':
            edge = 113
        elif letters == 'T':
            edge = 120
        elif letters == 'U':
            edge = 150
        elif letters == 'V':
            edge = 136
        elif letters == 'W':
            edge = 190
        elif letters == 'X':
            edge = 126
        elif letters == 'Y':
            edge = 119
        elif letters == 'Z':
            edge = 115


        inter, flat = (make_let_im('letter'+letters+'.png', plot_let = False, edge_pix = edge))
        flattened.append(flat)

    X = np.zeros((26,256))
    i = 0
    while i < 26:
        X[i,] = flattened[i]
        i += 1


    pca, Xproj, pca_comps = alphabet_pca(X, n_comp = n_comp)
    show_pca(Xproj, pca_comps, let_idx = let_idx)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
