import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# data_path = "./"
data_path = "/Users/dillanvictory/Documents/CS310/"
train_data = np.loadtxt(data_path + "mnist_train.csv", delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")

# Dataset preparation
train_input = np.array([np.array(d[1:]) for d in train_data])/255.0  # Normalize data
train_label = np.array([int(d[0]) for d in train_data])

test_input = np.array([np.array(d[1:]) for d in test_data])/255.0  # Normalize data
test_label = np.array([int(d[0]) for d in test_data])

def modelling(train_input, train_label, test_input, test_label):
    # determine the number of input features
    n_features = train_input.shape[1]

    # Create model
    model = Sequential([
        Dense(40, activation='sigmoid', input_shape=(n_features,)),
        Dense(40, activation='relu'),
        Dense(10, activation='softmax')

    ])

    # Compile the model
    opt = SGD(learning_rate=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_input, train_label, epochs=10, batch_size=32, verbose=1)

    # Evaluate the model
    loss, accuracy = model.evaluate(test_input, test_label, verbose=0)
    print(f'Test Accuracy: {accuracy*100}')

    return model

def visualisation(test_input, test_label, model):
    labelchoice = 0

    predictData = np.array(test_input[labelchoice])[None, ...]
    predictLabel = test_label[labelchoice]

    # make prediction
    yhat = model.predict(predictData)

    print("actual: ", predictLabel)

    # Display prediction
    print('Predicted: %s (class=%d)' % (yhat, np.argmax(yhat)))
    fig = plt.figure()
    plt.plot(yhat[0])
    plt.show()

# Example of how to use the modelling function
model = modelling(train_input, train_label, test_input, test_label)
visualisation(test_input, test_label, model)
