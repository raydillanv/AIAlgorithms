import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(target_digit):
    # Load the MNIST training and test datasets
    train_data_path = '/Users/dillanvictory/Documents/CS310/mnist_test.csv'
    test_data_path = '/Users/dillanvictory/Documents/CS310/mnist_train.csv'
    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    # Preprocess the training and test data
    # Now using the target_digit parameter to determine the digit to recognize
    train_labels = train_data.iloc[:, 0].apply(lambda x: 1 if x == target_digit else 0).values
    train_pixel_values = train_data.iloc[:, 1:].values

    test_labels = test_data.iloc[:, 0].apply(lambda x: 1 if x == target_digit else 0).values
    test_pixel_values = test_data.iloc[:, 1:].values

    class Perceptron(object):
        def __init__(self, no_inputs, target_digit, max_iterations=20, learning_rate=0.1):
            self.no_inputs = no_inputs
            self.target_digit = target_digit
            self.weights = np.zeros(no_inputs + 1)  # Including bias weight
            self.max_iterations = max_iterations
            self.learning_rate = learning_rate

        def predict(self, inputs):
            summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
            return 1 if summation > 0 else 0

        def train(self, training_data, labels):
            for _ in range(self.max_iterations):
                for inputs, label in zip(training_data, labels):
                    prediction = self.predict(inputs)
                    self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                    self.weights[0] += self.learning_rate * (label - prediction)

        def train_batch(self, training_data, labels):
            for _ in range(self.max_iterations):  # initialize variable for weight updates
                weight_updates = np.zeros(self.no_inputs + 1) # loop over training examples and labels
                for inputs, label in zip(training_data, labels):
                    prediction = self.predict(inputs) # predict output with inputs
                    weight_updates[1:] += (label - prediction) * inputs # bias as 1
                    weight_updates[0] += (label - prediction)
                self.weights[1:] += self.learning_rate * weight_updates[1:] / len(training_data)  # Update weights and bias with scaled average updates
                self.weights[0] += self.learning_rate * weight_updates[0] / len(training_data)

        def test(self, testing_data, labels):
            for inputs, label in zip(testing_data, labels):
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

    # Train the perceptron with the MNIST training data using the new batch method
    perceptron.train_batch(train_pixel_values, train_labels)

    # Visualize weights after training
    print(f"Weights after training for digit {target_digit}:")
    perceptron.visualize_weights()

    # Test the perceptron with the MNIST test data
    perceptron.test(test_pixel_values, test_labels)

# Example usage: pass the digit you want to train on and search for
#main(target_digit=7)
count = 0
while count != 10:
    main(target_digit=count)
    count += 1
