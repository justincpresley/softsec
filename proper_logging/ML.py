from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np
import mnist
import logging # import relevant info for logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical

# log in the beginning into the WORKSHOP2.log to allow logging all throughout this program.
logging.basicConfig(
    filename='WORKSHOP2.log',
    filemode='w',
    format='%(asctime)s.%(msecs)03d | %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

def readData():
    # since one of the main problems was related to poisioning attacks with data, Printing more information relating to the data
    # will help determine if its the problem.
    iris = datasets.load_iris()
    logging.info(f"Iris read: {iris.data} (type:{type(iris.data)}) | Iris Target: {iris.target} (type:{type(iris.target)})")
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    (type:{type(iris.data)})
    logging.info(f"Printing all data-frame information after this.")
    print(df.head())
    print(df.to_markdown())
    return df

def makePrediction():
    iris = datasets.load_iris()
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]
    prediction = knn.predict(X)
    # printing predictions will make the programmer know ahead of time generally how this ai will react.
    logging.info("Prediction being displayed after this.")
    print(prediction)

def doRegression():
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)


def doDeepLearning():
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()

    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5

    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    # printing ML variables is vital to improvement
    logging.info(f"Forming model (numfilters:{num_filters}, filtersize:{filter_size}, poolsize:{pool_size}).")
    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])

    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    # Train the model.
    logging.info("Training model with 3 epochs.")
    model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )

    # Does it finish? if so, tell me all the stuff you can about it to ensure long-term success
    logging.info("Saving weights 'cnn.h5'")
    model.save_weights('cnn.h5')
    predictions = model.predict(test_images[:5])
    logging.info("Printing test labels and other relevant info.")
    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]
    print(test_labels[:5]) # [7, 2, 1, 0, 4]


if __name__=='__main__':
    # Having Sections like this will allow us to know generally where we are at in the code. This helps future problems
    # associated with the code and allows the programmer to see how far data (if its poisionous) will make it in the program
    # so that we could make further changes to limit how far it goes.
    logging.info("* Entering Stage 'Reading Data'..")
    data_frame = readData()
    logging.info("* Entering Stage 'Making Predictions'..")
    makePrediction()
    logging.info("* Entering Stage 'Doing Regressions'..")
    doRegression()
    logging.info("* Entering Stage 'Deep Learning'..")
    doDeepLearning()
    logging.info("* Completed All Stages Successfully.")
