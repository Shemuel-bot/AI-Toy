import random
class Brain:
    def __init__ (self, layers_amount, neurons, input):
        self.input = input
        self.threshhold = 0.1
        self.layers = layers_amount
        self.neurons_amount = neurons
        self.brain = [[-random.random() if random.choice([True, False]) else random.random() for j in range(neurons) ] for i in range(layers_amount)]

    def run_layers (lyr1, lyr2):
        new_lyr = [0 for i in range(len(lyr1))]
        for i in range(len(lyr1)):
            for j in  lyr2:
                new_lyr[i] += (lyr1[i]+j)
        return new_lyr

    def compute (self, input):
        for i in range(len(self.brain)):
            input = Brain.run_layers(input, self.brain[i])
        return [i for i in input if i > self.threshhold]         

if __name__ == "__main__":
    brain = Brain(3, 3, [0.5, 0.2, 0.1])
    print(brain.compute([0.5, 0.2, 0.1]))
        