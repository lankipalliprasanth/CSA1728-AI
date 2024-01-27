import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, x):
        self.hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.output
    
    def backward(self, x, y, output):
        self.error = y - output
        self.delta_output = self.error * self.sigmoid_derivative(output)
        self.error_hidden = self.delta_output.dot(self.weights_hidden_output.T)
        self.delta_hidden = self.error_hidden * self.sigmoid_derivative(self.hidden_output)
        
        self.weights_hidden_output += self.hidden_output.T.dot(self.delta_output)
        self.bias_output += np.sum(self.delta_output, axis=0, keepdims=True)
        self.weights_input_hidden += x.T.dot(self.delta_hidden)
        self.bias_hidden += np.sum(self.delta_hidden, axis=0, keepdims=True)
        
    def train(self, x, y, epochs):
        for epoch in range(epochs):
            output = self.forward(x)
            self.backward(x, y, output)
            
    def predict(self, x):
        return self.forward(x)

# Example usage
if __name__ == "__main__":
    # Create a neural network with 2 input neurons, 3 hidden neurons, and 1 output neuron
    neural_net = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
    
    # Example dataset (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    # Train the neural network
    neural_net.train(X, y, epochs=10000)
    
    # Make predictions
    predictions = neural_net.predict(X)
    print("Predictions:")
    print(predictions)
