# AI-Toy

A simple prototype for an experimental neural network / evolutionary system in Python.

## Overview

This repository contains a lightweight proof-of-concept `Brain` class that combines a layered network structure with mutation-based evolution.

The code is intended as an early experiment rather than a production-ready machine learning project.

## What it does

- Defines a `Brain` model with a configurable number of layers and neurons
- Runs input data through chained layer computations
- Uses a basic mutation strategy to evolve a population of brains
- Evaluates fitness by comparing each brain's output with an expected answer

## Files

- `Prototype.py` - main prototype implementation and example evolutionary loop
- `README.md` - project overview and usage instructions

## Usage

Run the prototype with Python:

```bash
python Prototype.py
```

The script will initialize a population of brains, evolve them across generations, and print the best fitness score for each generation.

## Notes

- The current implementation uses a very simple layer combination strategy and a naive output selection mechanism.
- The evolutionary setup is meant for experimentation and may need refinement to improve learning behavior.
- Input handling and fitness evaluation are currently hard-coded for demonstration purposes.

## Next steps

Potential improvements include:

- implementing true weighted neuron activation functions
- adding configurable training data and fitness scenarios
- refining output decoding and prediction logic
- exploring crossover and more advanced evolutionary operators
