import random
import math
import difflib

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
        return [i for i in range(len(input)) if input[i] > self.threshhold]

    def mutate(self, mutation_rate=0.1, mutation_strength=0.5):
        """
        Mutate the neural network weights.
        
        Args:
            mutation_rate: Probability that each weight will be mutated (0.0 to 1.0)
            mutation_strength: Maximum amount a weight can change during mutation
        """
        for layer_idx in range(len(self.brain)):
            for neuron_idx in range(len(self.brain[layer_idx])):
                if random.random() < mutation_rate:
                    # Add random noise to the weight
                    mutation = random.uniform(-mutation_strength, mutation_strength)
                    self.brain[layer_idx][neuron_idx] += mutation
                    
                    # Optionally clamp weights to prevent them from growing too large
                    self.brain[layer_idx][neuron_idx] = max(-1.0, min(1.0, self.brain[layer_idx][neuron_idx]))


untokenized_input = [i for i in range(10)]

def evaluate_brain_fitness(brain, input, answer):
    brain_output = brain.compute(input)
    score = difflib.SequenceMatcher(None, brain_output, answer).ratio()
    return score

def evaluate_population(population, input, answer):
    fitness_scores = []
    for brain in population:
        fitness = evaluate_brain_fitness(brain, input, answer)
        fitness_scores.append(fitness)
    return fitness_scores

