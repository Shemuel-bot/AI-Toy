import random
import math
import difflib
import copy

class Brain:
    def __init__ (self, layers_amount, neurons, input):
        self.input = input
        self.threshhold = 0.1
        self.layers = layers_amount
        self.neurons_amount = neurons
        self.brain = [[-random.random() if random.choice([True, False]) else random.random() for j in range(neurons) ] for i in range(layers_amount)]

    # This function takes two layers of neurons and computes the output of the first layer as input to the second layer
    def run_layers (lyr1, lyr2):
        new_lyr = [0 for i in range(len(lyr1))]

        for i in range(len(lyr1)):
            for j in  lyr2:
                new_lyr[i] += (lyr1[i]+j)
        return new_lyr

    # This function takes an input and runs it through all the layers of the brain to produce an output
    def compute (self, input):
        input = [self.input[i] if i in input else 0 for i in range(len(self.input))]

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
tokenized_input = [random.random() for _ in range(10)]  # Example tokenized input

problem_set = [([0], [0])]

# Evaluate the fitness of a single brain based on how closely its output matches the expected answer
def evaluate_brain_fitness(brain, input, answer):
    brain_output = brain.compute(input)

    # Use difflib to calculate a similarity score between the brain's output and the expected answer
    score = difflib.SequenceMatcher(None, brain_output, answer).ratio()
    return score

# Evaluate the fitness of each brain in the population
def evaluate_population(population, input, answer):
    fitness_scores = []

    # Evaluate each brain and store its fitness score
    for brain in population:
        fitness = evaluate_brain_fitness(brain, input, answer)
        fitness_scores.append(fitness)

    # Find the brain with the highest fitness score and return it along with its score
    highest_fitness_idx = fitness_scores.index(max(fitness_scores))
    return fitness_scores[highest_fitness_idx], population[highest_fitness_idx]


def main():
    population_size = 100
    generations = 50
    mutation_rate = 0.1
    mutation_strength = 0.5

    # Create an initial population of brains
    population = [Brain(layers_amount=3, neurons=10, input=tokenized_input) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate population
        fitness, best_brain = evaluate_population(population, [0, 1], [0, 1])
        
        # Check if we found a solution with perfect fitness
        if fitness >= 1:
            print(f"Solution found in generation {generation + 1} with fitness {fitness:.4f}")
            break

        # Keep the best brain for the next generation
        new_population = [copy.deepcopy(best_brain.mutate(mutation_rate, mutation_strength)) for i in range(population_size)]  
        population = new_population

        # Print the best fitness score for this generation
        print(f"Generation {generation + 1}: Best Fitness = {fitness:.4f}")


if __name__ == "__main__":    main()
