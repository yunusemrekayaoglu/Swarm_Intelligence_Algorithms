
## 1. Particle Swarm Optimization in Python

This repository contains an implementation of the **Particle Swarm Optimization (PSO)** algorithm in Python. PSO is a nature-inspired optimization technique that simulates the social behavior of birds and fish to find optimal solutions in a given search space. This implementation is designed to minimize an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{D} X_i^2
\]

This function is a simple quadratic function, where the global minimum is located at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Particle Swarm Optimization (PSO)** algorithm works by initializing a population of candidate solutions (particles) that move around in the search space. Each particle adjusts its position based on its own experience and the experience of neighboring particles. The algorithm follows these main steps:

1. **Initialization**: Particles are randomly initialized within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: The objective function is evaluated for each particle to determine its fitness.
3. **Update Personal and Global Bests**: Each particle keeps track of its own best position (personal best) and the best position found by any particle (global best).
4. **Velocity Update**: Particles update their velocity based on their personal best and the global best.
5. **Position Update**: Particles update their positions based on their new velocities.
6. **Iteration**: Steps 2-5 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `pso()` Function

This function implements the Particle Swarm Optimization algorithm.

##### Parameters:
- `type`: The optimization type, either `"min"` for minimization (default) or `"max"` for maximization.
- `lb`: The lower bound of the search space for each dimension (default is `-5.12`).
- `ub`: The upper bound of the search space for each dimension (default is `5.12`).
- `D`: The dimensionality of the search space (default is `2`).
- `N`: The number of particles in the swarm (default is `30`).
- `c1`: The cognitive coefficient (default is `2`).
- `c2`: The social coefficient (default is `2`).
- `T`: The maximum number of iterations (default is `100`).
- `r1`: A random number for the cognitive component (default is `np.random.rand()`).
- `r2`: A random number for the social component (default is `np.random.rand()`).
- `w`: The inertia weight (default is `0.8`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the particles and evaluate their objective function values `F`.
2. **Personal Best Update**: Track the best position found by each particle (`pbest`) and the corresponding objective function values (`pbest_obj`).
3. **Global Best Update**: Determine the best position found by any particle (`gbest`) and its objective function value (`gbest_obj`).
4. **Velocity and Position Update**: For each iteration:
   - Update the velocity `v` of each particle based on its personal best position and the global best position.
   - Update the positions `X` of the particles based on their velocities.
   - Clip the positions to ensure they stay within the defined bounds.
   - Evaluate the objective function for each particle and update personal and global bests accordingly.

##### Output:
- The function returns the global best position and its corresponding objective function value.


## 2. Artificial Bee Colony Algorithm in Python

This repository contains an implementation of the **Artificial Bee Colony (ABC)** optimization algorithm in Python. ABC is a nature-inspired optimization technique based on the foraging behavior of honey bees, which efficiently explores the search space to find optimal solutions. This implementation minimizes an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{D} X_i^2
\]

This function is a simple quadratic function, where the global minimum is located at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Artificial Bee Colony (ABC)** algorithm simulates the foraging behavior of bees and consists of the following key components:

1. **Initialization**: A population of bees (candidate solutions) is randomly initialized within the defined bounds.
2. **Employed Bee Phase**: Employed bees explore the neighborhood of their current solutions and update them based on their fitness.
3. **Onlooker Bee Phase**: Onlooker bees select solutions based on their fitness and explore their neighborhoods.
4. **Scout Bee Phase**: Bees that have not improved their solutions after a certain number of iterations are replaced with new random solutions.
5. **Iteration**: The above phases are repeated for a specified number of iterations to find the optimal solution.

### Code Structure

#### `objective_function(x)`

This function computes the value of the objective function for a given input vector `x`.

##### Parameters:
- `x`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `x`.

#### `fitness_function(f)`

This function calculates the fitness value based on the objective function value.

##### Parameters:
- `f`: The objective function value.

##### Returns:
- A fitness score that is inversely related to the objective function value.

#### `roulette_wheel_selection(probabilities)`

This function implements the roulette wheel selection method to select an index based on probabilities.

##### Parameters:
- `probabilities`: An array of probabilities for selection.

##### Returns:
- An index chosen according to the probabilities.

#### `abc_algorithm()`

This function implements the Artificial Bee Colony optimization algorithm.

##### Parameters:
- `pop_size`: The total number of bees (default is `32`).
- `dimensions`: The number of dimensions in the search space (default is `2`).
- `lower_bound`: The lower bound of the search space for each dimension (default is `-5`).
- `upper_bound`: The upper bound of the search space for each dimension (default is `5`).
- `iterations`: The maximum number of iterations to perform (default is `100`).
- `limit_value`: The limit for the number of iterations without improvement (default is `10`).

##### Process:
1. **Initialization**: Randomly initialize the positions of the bees within the bounds and evaluate their objective function values.
2. **Employed Bees Phase**: Update each employed bee's position based on a randomly selected neighbor.
3. **Onlooker Bees Phase**: Compute selection probabilities based on fitness values and update the positions of the onlooker bees.
4. **Scout Bees Phase**: Replace bees that have not improved their positions after a specified number of iterations.
5. **Global Best Update**: Track and update the global best solution found.
6. **Store Best Values**: Keep a record of the best objective function values throughout the iterations.

##### Returns:
- The best objective function value found, the corresponding position, and a list of best values across iterations.





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
