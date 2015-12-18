from pattern_recog_func import *

#Works properly in the ipython notebook. Couldn't figure out why it returns an error
#when ran through terminal

bohr0 = mpimg.imread('bohr0.jpeg')
bohr1 = mpimg.imread('bohr1.jpeg')
bohr2 = mpimg.imread('bohr2.jpeg')
bohr3 = mpimg.imread('bohr3.jpeg')
bohr4 = mpimg.imread('bohr4.jpeg')
bohr5 = mpimg.imread('bohr5.jpeg')
bohr6 = mpimg.imread('bohr6.jpeg')
bohr7 = mpimg.imread('bohr7.jpeg')
bohr8 = mpimg.imread('bohr8.jpeg')
bohr9 = mpimg.imread('bohr9.jpeg')

ein0 = mpimg.imread('ein0.jpeg')
ein1 = mpimg.imread('ein1.jpeg')
ein2 = mpimg.imread('ein2.jpeg')
ein3 = mpimg.imread('ein3.jpeg')
ein4 = mpimg.imread('ein4.jpeg')
ein5 = mpimg.imread('ein5.jpeg')
ein6 = mpimg.imread('ein6.jpeg')
ein7 = mpimg.imread('ein7.jpeg')
ein8 = mpimg.imread('ein8.jpeg')
ein9 = mpimg.imread('ein9.jpeg')
ein10 = mpimg.imread('ein10.jpeg')

physicists = []
y = []
phys_dict = {0: 'Bohr', 1: 'Einstein'}

for x in range(0,10):
    bohr_int = interpol_im('bohr'+str(x)+'.jpeg', dim1 = 45, dim2 = 60)
    physicists.append(bohr_int)
    y.append(0)
for j in range(0,11):
    ein_int = interpol_im('ein'+str(j)+'.jpeg', dim1 = 45, dim2 = 60)
    physicists.append(ein_int)
    y.append(1)

physicists = np.array(physicists)
X = np.vstack(physicists)

correct = 0
for z in range(len(y)):
    Xtrain = np.delete(X, z, axis = 0)
    ytrain = np.delete(y, z)
    Xcheck = X[z].reshape(1,-1)
    md_pca, Xproj = pca_X(Xtrain)
    
    Xtrain_proj = md_pca.transform(Xtrain)
    Xcheck_proj = md_pca.transform(Xcheck)
    
    md_train = svm_train(Xtrain_proj, ytrain)
    answer = md_train.predict(Xcheck_proj)[0]
    
    if answer != y[z]:
        correct += 1

success = (correct/ len(physicists))
print('Succes rate: {:0.2%}'.format(success))


unseen1 = pca_svm_pred('unseen_phys1.jpg', md_pca, md_train)
unseen2 = pca_svm_pred('unseen_phys2.jpg', md_pca, md_train)

print('PCA+SVM prediction for physicist 1: ', phys_dict[unseen1])
print('PCA+SVM prediction for physicist 2: ', phys_dict[unseen2])