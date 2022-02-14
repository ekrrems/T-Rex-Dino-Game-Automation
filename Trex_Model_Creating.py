import glob 
import os
import numpy as np
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from keras.preprocessing.image import img_to_array,array_to_img,load_img
from PIL import Image
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split


imgs = glob.glob(r'C:\Users\ekrem\OneDrive\Masaüstü\ML Projects\T-rex Game\imgs\*.png')


w = 125
h = 50

X = []
y = []

filename = os.path.basename(imgs[0])
label = filename.split('_')[0]
print(filename)


for img in imgs:
    filename = os.path.basename(img)
    label = filename.split('_')[0]
    im = Image.open(img).convert('L')
    im = np.array(im)
    im = np.resize(im,(w,h))
    im = im/255
    X.append(im)
    y.append(label)
    
X = np.array(X)
X = X.reshape((X.shape[0],X.shape[1],X.shape[2],1))

print(y)
sns.countplot(y)

def one_hot_labels (values):
    le = LabelEncoder()
    label_encoded = le.fit_transform(values)
    onehot_encoder = OneHotEncoder(sparse=False)
    label_encoded = label_encoded.reshape((len(label_encoded),1))
    onehot_encoded = onehot_encoder.fit_transform(label_encoded)
    return onehot_encoded

y=one_hot_labels(y)
print(y[0:5])
    
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,
                                                 random_state=2)
print("""
      Shape of X Train:{}
      Shape of y Train:{}
      Shape of X Test :{}
      Shape of y Test :{}
      """.format(X_train.shape,y_train.shape,X_test.shape,y_test.shape))



model = Sequential() 

model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(w,h,1)))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(3,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='Adam',
              metrics=['accuracy'])

model.fit(X_train,y_train,epochs=35,batch_size=64)

score_train = model.evaluate(X_train,y_train)
print('Training Accuracy :'+str(score_train[1]*100))

score_test = model.evaluate(X_test,y_test)
print('Test Accuracy :'+str(score_test[1]*100))

model.save('C:\\Users\\ekrem\\OneDrive\\Masaüstü\\ML Projects\\T-rex Game\\trex_weight.h5')













    
    
    