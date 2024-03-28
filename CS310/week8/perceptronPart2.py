import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(target_digit):
    # Load MNIST training and test files
    train_data_path = '/Users/dillanvictory/Documents/CS310/mnist_test.csv'
    test_data_path = '/Users/dillanvictory/Documents/CS310/mnist_train.csv'
    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    # Preprocess the training and test data
    # use target_digit to determine the digit to recognize
    train_labels = train_data.iloc[:, 0].apply(lambda x: 1 if x == target_digit else 0).values
    train_pixel_values = train_data.iloc[:, 1:].values

    test_labels = test_data.iloc[:, 0].apply(lambda x: 1 if x == target_digit else 0).values
    test_pixel_values = test_data.iloc[:, 1:].values

    class Perceptron(object):
        def __init__(self, no_inputs, target_digit, max_iterations=20, learning_rate=0.1):
            self.no_inputs = no_inputs
            self.target_digit = target_digit
            self.weights = np.zeros(no_inputs + 1)  # bias weight
            self.max_iterations = max_iterations
            self.learning_rate = learning_rate

        def predict(self, inputs):
            summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
            return 1 if summation > 0 else 0 # to return if within threshold

        def train(self, training_data, labels):
            for _ in range(self.max_iterations):
                for inputs, label in zip(training_data, labels): # iterate through training data for number of iterations
                    prediction = self.predict(inputs)
                    self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                    self.weights[0] += self.learning_rate * (label - prediction)

        def test(self, testing_data, labels):
            for inputs, label in zip(testing_data, labels): # iterate through testing data for number of iterations
                prediction = self.predict(inputs)
                recognized = str(self.target_digit) if prediction == 1 else 'other'
                print(f"recognized {recognized}")


        def visualize_weights(self):
            plt.imshow(self.weights[1:].reshape(28, 28), cmap='gray', interpolation='none')
            plt.colorbar()
            plt.title(f"Visualization of Weights for Digit {self.target_digit}")
            plt.show()

    # Initialize the Perceptron with the target digit
    perceptron = Perceptron(no_inputs=784, target_digit=target_digit, max_iterations=10, learning_rate=0.01)

    # Visualize weights before training
    print(f"Weights before training for digit {target_digit}:")
    perceptron.visualize_weights()

    # perceptron with MNIST training data
    perceptron.train(train_pixel_values, train_labels)

    # after training
    print(f"Weights after training for digit {target_digit}:")
    perceptron.visualize_weights()

    # perceptron with MNIST test data
    perceptron.test(test_pixel_values, test_labels)

# 0-9 test
#main(target_digit=7)
count = 0;
while count != 10:
    main(target_digit=count)
    count += 1
