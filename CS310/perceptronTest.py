import numpy as np

class Perceptron(object):
    def __init__(self, no_inputs, max_iterations=20, learning_rate=0.1):
        self.no_inputs = no_inputs
        self.weights = np.zeros(no_inputs + 1)  # Including bias weight
        self.max_iterations = max_iterations
        self.learning_rate = learning_rate
        self.print_details()

    def print_details(self):
        print("No. inputs:", self.no_inputs)
        print("Max iterations:", self.max_iterations)
        print("Learning rate:", self.learning_rate)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Bias is weights[0] take input to calculate weighted sum
        return 1 if summation > 0 else 0 # to return if within threshold

    def train(self, training_data, labels):
        print("Weights at start of training:", np.round(self.weights, 8))  # Print initial weights
        for _ in range(self.max_iterations): # iterate through training data for number of iterations
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)  # Bias update
            print("Weights after:", np.round(self.weights, 8))  # Print weights after each epoch

    def test(self, testing_data, labels):
        correct_predictions = 0
        for inputs, label in zip(testing_data, labels): # iterate through testing data for number of iterations
            prediction = self.predict(inputs)
            print(f"actual {label} est {prediction}")
            if prediction == label:
                correct_predictions += 1
        accuracy = correct_predictions / len(testing_data) * 100
        print("Accuracy:", accuracy)
        return accuracy

# Test the Perceptron class with a simple logic gate dataset
# Choose AND logic gate with an added bias input
# Inputs: [Input1, Input2, Bias]
# Output: AND operation result
training_data = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])
labels = np.array([0, 0, 0, 1])  # AND operation results

# perceptron with 3 inputs (including the bias), 5 iterations, and a learning rate of 0.1
perceptron = Perceptron(no_inputs=3, max_iterations=7, learning_rate=0.1)

# before training
print("Testing before training:")
perceptron.test(testing_data=training_data, labels=labels)

# train perceptron
print("\nTraining:")
perceptron.train(training_data=training_data, labels=labels)

# after training
print("\nTesting after training:")
perceptron.test(testing_data=training_data, labels=labels)
