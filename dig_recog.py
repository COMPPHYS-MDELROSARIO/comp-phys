from pattern_recog_func import *
dig_data = load_digits()
X = dig_data.data
X_img = dig_data.images
y = dig_data.target
x_range = X[0:60]
y_range = y[0:60]
beg = 60
end = 80
md_train = svm_train(x_range,y_range)
misid = 0

for i in range(beg, end):
    pred = ((md_train.predict(X)[i]).reshape(1,-1)[0])
    answer = y[i]
    if pred[0] != answer:
        misid += 1
        print('index, actual digit, svm_predition', i, y[i], pred[0])
success = (end - beg - misid)/(end-beg)


print('Total number of mis-identifications {:d}'.format(misid))
#Success rate works properly in the ipython notebook. Not sure why it shows up as zero
#when run in terminal
print('Succes rate: {:0.2%}'.format(success))

unseen = mpimg.imread('unseen_dig.png')
unseen_int = interpol_im('unseen_dig.png', dim1 = 8, dim2 = 8, plot_new_im = True, axis_off = True)
#unseen_int = interpol_im(X[15], dim1 = 8, dim2 = 8, plot_new_im = True)
plt.figure(figsize = (4,4))
plt.title('Image from data set')
plt.imshow(X_img[15], cmap = 'binary')
plt.grid('off')
plt.axis('off')

scaled = rescale_pixel(X, unseen_int, ind = 15)

unseen_int_pre = md_train.predict(unseen_int)
scaled_pre = md_train.predict(scaled)
print ('Prediction of unseen: {:d}'.format(unseen_int_pre[0]))
print('Prediction of scaled unseen: {:d}'.format(scaled_pre[0]))