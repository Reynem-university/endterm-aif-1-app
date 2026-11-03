# Chapter 3. Rocky Peaks and Local Optimization

## 3.1 State Space Search: Hill Climbing and Its Traps

Emerging from the forest, Mario and ROBO-LUMA confronted the sheer cliffs of the Rocky Peaks. There was no pre-mapped road map or node graph here; to reach the pass, the robot had to climb to the highest plateau under conditions of thin air and limited visibility.

Luigi activated the Hill Climbing algorithm: — Imagine, Mario, that a robot is standing blindfolded on a mountainside. Its task is to always take a step in the direction of the neighbor whose height is greater than the current one. The height function here acts as the objective function f(s).

However, Mario quickly noticed the vulnerability of this method when the robot froze on a small ledge and stopped moving forward: — Hey, Luigi, it just stopped! Why isn't it moving anywhere?

The engineer nodded: — Because Hill Climbing is a greedy local search algorithm. It inevitably runs into three classic topological traps:

1. Local Maxima: A peak that is higher than all its immediate neighbors, but significantly lower than the global peak of the mountain. The robot thinks it has reached the goal because any step from here leads downward.
2. Plateaus: Flat areas of terrain where all neighboring points have the exact same height. On a plateau, the slope steepness (gradient) is zero, and the algorithm loses its direction of movement.
3. Ridges: Narrow inclined crests. In such places, steps strictly along coordinate axes lead downward, while diagonal climbing is blocked by neighborhood rules, causing the robot to frantically "bounce" from side to side.

## 3.2 Simulated Annealing Algorithm

To rescue the robot from getting stuck in local dead ends, Luigi loaded the Simulated Annealing algorithm into its memory, mathematically inspired by the slow cooling process of metals during hardening.

— The idea is to occasionally allow the robot to take worsening steps (walking down the slope), — Luigi explained. — At the start, the system temperature is high, and the robot can make bold jumps to explore the entire map (Exploration). As cooling progresses, the probability of bad moves drops, and the robot focuses on fine-tuning its position (Exploitation).

The probability of accepting a worse state is determined by the Boltzmann distribution:

```
P(accept)=eTΔE
```

where ΔE=E(snext)−E(scurrent) is the height increment (negative during deterioration), and T is the current system temperature.

```python
import math
import random
def simulated_annealing(objective_func, initial_state, temp_schedule):
 current_state = initial_state
 current_val = objective_func(current_state)
 for T in temp_schedule:
     if T <= 1e-5:
         break
     # Generate a random neighbor in the vicinity
     neighbor = current_state + random.uniform(-1.0, 1.0)
     neighbor_val = objective_func(neighbor)
     delta = neighbor_val - current_val # If the new state is better OR passes the Boltzmann probability barrier
     if delta > 0 or random.random() < math.exp(delta / T):
         current_state = neighbor
         current_val = neighbor_val
 return current_state, current_val
```

![Место для изображения: график остывания / имитация отжига](assets/chapter3.jpg)

## 3.3 Genetic Algorithms: Evolution of Solutions

To precisely tune the parameters of the robot's leg hydraulic actuators when climbing steep, loose stones, Luigi applied a Genetic Algorithm. A multitude of suspension setting variants were encoded as digital chromosomes.

The evolutionary process consisted of four continuous steps:

1. Fitness Evaluation: Each individual is tested on the slope; the Fitness(x) function measures climbing speed and stability.
2. Selection: The best specimens are selected to reproduce using tournament selection or roulette wheel selection.
3. Crossover: Parent chromosomes exchange code segments, producing offspring with combined properties.
4. Mutation: Random inversion of individual genes with a low probability pm, preventing premature convergence of the population to a single local standard.

Thanks to evolutionary trials, ROBO-LUMA's suspension adapted to the rocky terrain, and the robot successfully conquered the peaks, opening the gates to the gloomy World 4.
