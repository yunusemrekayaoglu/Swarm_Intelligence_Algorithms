



## 3. Grey Wolf Optimizer in Python

This repository contains an implementation of the **Grey Wolf Optimizer (GWO)** in Python. The GWO is a nature-inspired metaheuristic optimization algorithm, which simulates the hunting behavior of grey wolves. This implementation is applied to a 2D optimization problem where the objective is to minimize a quadratic function.

### Objective Function

The objective function for this example is:

\[
f(x) = (x_0 - 5)^2 + (x_1 - 2)^2
\]

This is a simple quadratic function where the global minimum is located at \(x = [5, 2]\).

### Algorithm Overview

The **Grey Wolf Optimizer (GWO)** simulates the social hierarchy and hunting strategy of grey wolves. The hierarchy consists of:

1. **Alpha**: The leader of the pack, which represents the best solution found so far.
2. **Beta**: The second-best solution, assisting the alpha in decision-making.
3. **Delta**: The third-best solution, subordinate to alpha and beta.

Other wolves follow these leaders and update their positions based on the distance to the alpha, beta, and delta wolves. The wolves search for prey (i.e., the optimal solution) by updating their positions using three main steps:

1. **Encircling prey**: The wolves estimate the location of the prey.
2. **Hunting**: The wolves adjust their positions based on the best-known solutions.
3. **Attacking**: As the wolves close in on the prey, the exploration parameter decreases, focusing more on exploitation of the search space.

### Code Structure

#### `grey_wolf()` Function

This function implements the Grey Wolf Optimizer (GWO). 

##### Parameters:
- `run`: The number of independent runs to perform. Default is `30`.
- `N`: The population size (number of wolves). Default is `20`.
- `lb`: The lower bound of the search space for each dimension. Default is `-10`.
- `ub`: The upper bound of the search space for each dimension. Default is `10`.
- `T`: The maximum number of iterations per run. Default is `100`.
- `D`: The dimensionality of the search space. Default is `2` (this implementation uses a 2D space).

##### Process:
1. **Initialization**: The positions of the wolves are randomly initialized within the bounds `[lb, ub]`.
2. **Wolf Hierarchy**: The objective function values for each wolf are calculated, and the wolves are sorted based on their performance (fitness). The top three wolves are assigned to alpha, beta, and delta.
3. **Position Update**: In each iteration, the positions of the wolves are updated based on the influence of alpha, beta, and delta. Random coefficients are used to simulate the wolves' exploration of the search space.
4. **Bounds Checking**: The positions are clipped to ensure they stay within the defined bounds.
5. **Result Tracking**: At the end of each run, the best solution found (alpha wolf) is saved.

##### Output:
- The algorithm prints the best solution (position of the alpha wolf) and the corresponding function value for each run.
- The mean and standard deviation of the best solutions across all runs are also printed.
