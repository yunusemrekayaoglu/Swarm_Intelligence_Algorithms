
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





## 4. Whale Optimization Algorithm in Python

This repository contains an implementation of the **Whale Optimization Algorithm (WOA)** in Python. WOA is a nature-inspired optimization technique that simulates the hunting behavior of humpback whales to find optimal solutions in a given search space. This implementation is designed to minimize an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{D} X_i^2
\]

This function is a simple quadratic function, where the global minimum is located at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Whale Optimization Algorithm (WOA)** works by initializing a population of candidate solutions (whales) that explore the search space. The algorithm follows these main steps:

1. **Initialization**: Whales are randomly initialized within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: The objective function is evaluated for each whale to determine its fitness.
3. **Update Best Solutions**: The best solution among the whales is tracked.
4. **Position Update**: Whales update their positions based on their best solution and the best solutions of others.
5. **Iteration**: Steps 2-4 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `whale_optimization()` Function

This function implements the Whale Optimization Algorithm.

##### Parameters:
- `lb`: The lower bound of the search space for each dimension (default is `-5.12`).
- `ub`: The upper bound of the search space for each dimension (default is `5.12`).
- `dim`: The dimensionality of the search space (default is `2`).
- `N`: The number of whales in the population (default is `30`).
- `T`: The maximum number of iterations (default is `100`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the whales and evaluate their objective function values `F`.
2. **Best Solution Tracking**: Track the best position found by any whale (`Xbest`) and its corresponding objective function value (`Fbest`).
3. **Position Update**: For each iteration:
   - Update the positions of the whales based on their best solution and the behavior of other whales.
   - Apply boundary constraints to ensure the positions remain within the defined limits.
   - Evaluate the objective function for each whale and update the best solution accordingly.

##### Output:
- The function returns the global best position and its corresponding objective function value, along with the fitness values over iterations.

### Results

The results of the optimization can be visualized through a plot of the fitness values over iterations, showing the convergence behavior of the algorithm.



## 5. Mouse Swarm Optimization in Python

This repository contains an implementation of the **Mouse Swarm Optimization (MSO)** algorithm in Python. MSO is a population-based optimization technique inspired by the social behavior of mice, aiming to find optimal solutions within a defined search space. This implementation minimizes an objective function, defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{D} X_i^2
\]

This function is a simple quadratic function, where the global minimum is located at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Mouse Swarm Optimization (MSO)** algorithm works by initializing a population of candidate solutions (mice) that move around in the search space. Each mouse updates its position based on its distance from the best-known position and a random adjustment factor. The algorithm follows these main steps:

1. **Initialization**: Mice are randomly positioned within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: The objective function is evaluated for each mouse to determine its fitness.
3. **Update Best Position**: Track the best position (`Pr`) found by any mouse and its corresponding fitness value (`fitbest`).
4. **Position Update**: Each mouse’s position is adjusted based on a calculated random value `R` and an adjustment factor `A`, which decreases over time.
5. **Iteration**: Steps 2-4 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `mouse_swarm()` Function

This function implements the Mouse Swarm Optimization algorithm.

##### Parameters:
- `N`: The number of mice in the swarm (default is `30`).
- `T`: The maximum number of iterations (default is `100`).
- `lb`: The lower bound of the search space for each dimension (default is `-5`).
- `ub`: The upper bound of the search space for each dimension (default is `5`).
- `D`: The dimensionality of the search space (default is `2`).

##### Process:
1. **Initialization**: Randomly initialize the positions `P` of the mice and evaluate their objective function values `fit`.
2. **Best Position Update**: Track the best position found by any mouse (`Pr`) and its corresponding objective function value (`fitbest`).
3. **Position Update**: For each iteration:
   - Calculate the adjustment factor `A` and random component `R` for each mouse.
   - Update each mouse’s position based on its current position, the best position, and the adjustment factor.
   - Clip the positions to ensure they stay within the defined bounds.
   - Evaluate the objective function for each mouse and update the best position if a new best is found.

##### Output:
- The function prints the best objective function value found (`fitbest`) and the corresponding position (`Pr`).


## 6. Grey Wolf Optimization in Python

This repository contains an implementation of the **Grey Wolf Optimization (GWO)** algorithm in Python. GWO is a nature-inspired optimization technique that simulates the social hierarchy and hunting behavior of grey wolves to find optimal solutions within a defined search space. This implementation minimizes an objective function.

### Objective Function

The objective function for this example is defined as:

\[
f(x) = (x[0] - 5)^2 + (x[1] - 2)^2
\]

This function has its global minimum located at \(x = [5, 2]\).

### Algorithm Overview

The **Grey Wolf Optimization (GWO)** algorithm mimics the hunting behavior of grey wolves, which organize themselves into social hierarchies. The algorithm uses a population of candidate solutions (wolves) and adjusts their positions according to the best-known solutions, following these main steps:

1. **Initialization**: Wolves are randomly initialized within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: Each wolf’s fitness is evaluated by calculating the objective function.
3. **Hierarchy Setup**: The top three wolves with the best fitness values are assigned roles as alpha, beta, and delta wolves, while the remaining wolves are considered omegas.
4. **Position Update**: Wolves update their positions based on their distances from the alpha, beta, and delta wolves, incorporating random adjustments for exploration.
5. **Iteration**: Steps 2-4 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(x)` Function

This function computes the objective function value for a given input vector `x`.

##### Parameters:
- `x`: A numpy array representing the input vector.

##### Returns:
- The objective function value based on `x`.

#### `grey_wolf()` Function

This function implements the Grey Wolf Optimization algorithm.

##### Parameters:
- `run`: Number of independent runs (default is `30`).
- `N`: Number of wolves in the population (default is `20`).
- `lb`: The lower bound of the search space (default is `-10`).
- `ub`: The upper bound of the search space (default is `10`).
- `T`: Maximum number of iterations per run (default is `100`).
- `D`: Dimensionality of the search space (default is `2`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the wolves within the specified bounds.
2. **Fitness Evaluation and Sorting**: Calculate the objective function for each wolf and sort them to identify the alpha, beta, and delta wolves.
3. **Position Update**: For each wolf, adjust its position based on its distance from the alpha, beta, and delta wolves using randomly generated coefficients `A` and `C`.
   - Calculate distances to alpha, beta, and delta wolves.
   - Adjust each dimension of the position based on the weighted average of these three distances.
4. **Boundary Enforcement**: Clip each wolf’s position to ensure it remains within the bounds, then recalculate the objective function.
5. **Hierarchy Update**: Update the positions of alpha, beta, and delta wolves based on the new best solutions found.
6. **Run Statistics**: At the end of each run, print the best solution and objective function value for the alpha wolf.

#### Output:
- Prints the best objective function value found (`f_alpha`) and the corresponding position (`X_alpha`) at the end of each run.
- Prints the average and standard deviation of the best solutions across all runs.



## 7. Salp Swarm Optimization in Python

This repository contains an implementation of the **Salp Swarm Optimization (SSO)** algorithm in Python. SSO is a nature-inspired optimization technique that simulates the movement and swarming behavior of salps to find optimal solutions within a search space. This implementation is designed to minimize an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{D} X_i^2
\]

This function has its global minimum at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Salp Swarm Optimization (SSO)** algorithm models the swarming behavior of salps, where each salp adjusts its position based on its relative location in the swarm and the best-known position in the search space. The algorithm follows these main steps:

1. **Initialization**: Salps are randomly initialized within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: Each salp’s fitness is evaluated by calculating the objective function.
3. **Best Position Tracking**: Track the best position (`F`) and corresponding fitness value (`fitBest`) found by any salp.
4. **Position Update**: Each salp’s position is updated based on its distance from the best position, incorporating random coefficients for exploration.
5. **Iteration**: Steps 2-4 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `salp_optimization()` Function

This function implements the Salp Swarm Optimization algorithm.

##### Parameters:
- `N`: Number of salps in the swarm (default is `20`).
- `T`: Maximum number of iterations (default is `100`).
- `lb`: The lower bound of the search space (default is `-5`).
- `ub`: The upper bound of the search space (default is `5`).
- `D`: Dimensionality of the search space (default is `2`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the salps within the specified bounds.
2. **Best Position Tracking**: Track the best position found by any salp (`F`) and the corresponding objective function value (`fitBest`).
3. **Position Update**:
   - **Leader Salps**: For each leader salp (first half of the population), update positions based on the best-known position and random coefficients.
   - **Follower Salps**: For each follower salp (second half of the population), update positions based on the position of the preceding salp.
   - Update the exponential coefficient `c1` based on the current iteration to control the exploration-exploitation trade-off.
4. **Boundary Enforcement**: Clip the positions to ensure they remain within bounds, then evaluate the objective function and update the best position if a new best is found.

##### Output:
- The function prints the best objective function value found (`fitBest`) and the corresponding position (`F`) at the end of the optimization.




## 8. Remora Optimization in Python

This repository contains an implementation of the **Remora Optimization (Remora Opt)** algorithm in Python. The Remora Opt algorithm is a nature-inspired optimization technique that simulates the behavior of remoras, small fish that attach themselves to larger hosts (such as sharks) to navigate the ocean more efficiently. This implementation minimizes an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{\text{Dim}} X_i^2
\]

This function has its global minimum at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Remora Optimization (Remora Opt)** algorithm models remoras' behavior, which balance between following the best-known position in the search space and exploring new positions. The algorithm follows these main steps:

1. **Initialization**: Remoras are randomly initialized within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Evaluation**: Each remora’s fitness is evaluated by calculating the objective function.
3. **Best Position Tracking**: Track the best position (`Rbest`) and corresponding fitness value (`fitBest`) found by any remora.
4. **Position Update**: Each remora’s position is updated based on its current position, previous position, and the best-known position.
5. **Iteration**: Steps 2-4 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `remore_opt()` Function

This function implements the Remora Optimization algorithm.

##### Parameters:
- `N`: Number of remoras in the population (default is `50`).
- `Dim`: Dimensionality of the search space (default is `2`).
- `lb`: The lower bound of the search space (default is `-100`).
- `ub`: The upper bound of the search space (default is `100`).
- `C`: Attraction coefficient (default is `0.1`).
- `T`: Maximum number of iterations (default is `200`).

##### Process:
1. **Initialization**: Randomly initialize the positions `R` of the remoras within the specified bounds.
2. **Best Position Tracking**: Track the best position found by any remora (`Rbest`) and the corresponding objective function value (`fitBest`).
3. **Position Update**:
   - **Leader Remora**: For each leader remora, update position based on the best-known position, with a probabilistic approach that includes random coefficients for exploration.
   - **Random Influence**: Some remoras adjust their position by referencing the best-known position (`Rbest`) and another randomly chosen remora.
   - **Velocity Adjustment**: For remoras that do not meet the best fitness, update position using a velocity parameter `V` that decreases as the iterations progress, helping balance exploration and exploitation.
4. **Boundary Enforcement**: Clip the positions to ensure they remain within bounds, then evaluate the objective function and update the best position if a new best is found.

##### Output:
- The function prints the best objective function value found (`fitBest`) at the end of the optimization.


## 9. Honey Badger Optimization in Python

This repository contains an implementation of the **Honey Badger Optimization (HBO)** algorithm in Python. HBO is a bio-inspired optimization algorithm that simulates the foraging behavior of honey badgers, which employ tactics of digging and targeting prey to efficiently search for food. This implementation minimizes an objective function defined as the sum of squares of the input variables.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{\text{Dim}} X_i^2
\]

This function has its global minimum at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Honey Badger Optimization (HBO)** algorithm mimics honey badgers’ foraging strategy, alternating between digging for prey and consuming honey. It proceeds through the following steps:

1. **Initialization**: The honey badgers are initialized randomly within the bounds defined by `lb` (lower bound) and `ub` (upper bound).
2. **Prey Identification**: The position of the prey (`X_prey`) is identified as the honey badger with the lowest objective function value.
3. **Position Update**: Each honey badger updates its position using either a **digging** phase or a **honey consumption** phase, determined by a random probability.
4. **Iteration**: Steps 2-3 are repeated for a defined number of iterations (`T`).

### Code Structure

#### `obj(X)` Function

This function computes the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `honey_badger_optimization()` Function

This function implements the Honey Badger Optimization algorithm.

##### Parameters:
- `N`: Number of honey badgers in the population (default is `20`).
- `beta`: Amplification factor in the digging phase (default is `6`).
- `C`: Attraction coefficient (default is `2`).
- `T`: Maximum number of iterations (default is `500`).
- `Dim`: Dimensionality of the search space (default is `2`).
- `ub`: Upper bound of the search space (default is `10`).
- `lb`: Lower bound of the search space (default is `-10`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the honey badgers within the specified bounds.
2. **Prey Identification**: Identify the prey (`X_prey`) as the honey badger with the best fitness (smallest objective function value).
3. **Position Update**:
   - **Digging Phase**: Each honey badger updates its position based on a set of random parameters and the prey's position to simulate the digging behavior.
   - **Honey Consumption Phase**: Each honey badger adjusts its position toward the prey in smaller increments to simulate energy conservation while consuming honey.
4. **Boundary Enforcement**: Clip the positions to ensure they remain within bounds, then evaluate the objective function and update the best position if a new best is found.

##### Output:
- The function prints the best objective function value found (`F_prey`) and the corresponding position (`X_prey`) at the end of the optimization.


## 10. Kingfisher Optimization in Python

This repository contains an implementation of the **Kingfisher Optimization (KO)** algorithm in Python. KO is a metaheuristic optimization algorithm inspired by the foraging and survival strategies of kingfishers. This algorithm leverages unique strategies to locate the global optimum of a given objective function, specifically minimizing the sum of squared inputs.

### Objective Function

The objective function for this example is defined as:

\[
f(X) = \sum_{i=1}^{\text{Dim}} X_i^2
\]

This function has its global minimum at \(X = [0, 0, \ldots, 0]\).

### Algorithm Overview

The **Kingfisher Optimization (KO)** algorithm is inspired by the hunting behavior of kingfishers and has two primary phases: exploration and exploitation. These phases are represented by movement strategies to optimize the solution over a set number of iterations.

1. **Initialization**: A population of kingfishers is randomly initialized within specified bounds (`lb` and `ub`).
2. **Exploration and Exploitation**: For each iteration, kingfishers update their positions based on their neighbors and the best known position in the population.
3. **Behavioral Adjustment**: Each kingfisher adjusts its movement strategies based on different factors, simulating the hunting efficiency of the kingfisher.
4. **Iteration**: Steps 2-3 are repeated for a specified number of iterations (`Tmax`).

### Code Structure

#### `obj(X)` Function

This function calculates the objective function value for a given input vector `X`.

##### Parameters:
- `X`: A numpy array representing the input vector.

##### Returns:
- The sum of squares of the elements in `X`.

#### `kingfisher_optimization()` Function

This function implements the Kingfisher Optimization algorithm.

##### Parameters:
- `N`: Number of kingfishers in the population (default is `20`).
- `Tmax`: Maximum number of iterations (default is `500`).
- `Dim`: Dimensionality of the search space (default is `2`).
- `ub`: Upper bound of the search space (default is `10`).
- `lb`: Lower bound of the search space (default is `-10`).
- `BF`: A parameter that controls the exploration behavior (default is `8`).

##### Process:
1. **Initialization**: Randomly initialize the positions `X` of the kingfishers within the defined bounds.
2. **Exploration and Exploitation**: Each kingfisher updates its position by either simulating pursuit behavior or a random attraction towards other kingfishers.
   - **Pursuit Movement**: Kingfishers adjust positions based on a "pursuit" of the best-found solution and other individuals.
   - **Random Movement**: Kingfishers move based on random interactions with neighbors, exploring the search space.
3. **Boundary Enforcement**: Clip the positions to remain within the bounds, evaluate the objective function, and update the best solution if a new best is found.

##### Output:
- The function prints the best objective function value found (`fbest`) and the corresponding position (`Xbest`) at the end of the optimization.



