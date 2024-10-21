"""pr.7 Implement feed forward back propagation neural network learning algorithm."""

import numpy as np

class NeuralNetwork:
    def __init__(self):
        np.random.seed(0)  # Seed for reproducibility
        # Initialize weights randomly
        self.weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))  # Sigmoid activation function

    def sigmoid_derivative(self, x):
        return x * (1 - x)  # Derivative of the sigmoid function

    def train(self, inputs, outputs, iterations):
        for _ in range(iterations):
            output = self.think(inputs)  # Get the output from the network
            error = outputs - output  # Calculate error
            adjustments = np.dot(inputs.T, error * self.sigmoid_derivative(output))  # Calculate adjustments
            self.weights += adjustments  # Update weights

    def think(self, inputs):
        return self.sigmoid(np.dot(inputs, self.weights))  # Calculate output

if __name__ == "__main__":
    nn = NeuralNetwork()  # Create a neural network instance

    # Training data: 4 examples, 3 inputs, 1 output
    training_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_outputs = np.array([[0], [1], [1], [0]])

    nn.train(training_inputs, training_outputs, 15000)  # Train the network

    # Get user input for prediction
    user_input = [float(input(f"User Input {i + 1} (0 or 1): ")) for i in range(3)]
    print("New output data:", nn.think(np.array(user_input)))  # Output prediction
