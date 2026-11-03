# Chapter 5. The Ice Dungeon — Markov Decision Processes (MDP)

## 5.1 Mathematical Model of MDPs

Descending into World 5, the heroes found themselves in a huge underground grotto covered with a mirror layer of ice. When ROBO-LUMA took a step forward, the slippery surface shifted its trajectory: instead of the target cell, the robot landed in the correct cell with a probability of 0.8, but slid to the left with a probability of 0.1 and to the right with a probability of 0.1.

— Deterministic search algorithms are useless here, Mario, — Luigi sighed. — We have encountered a stochastic environment. Such problems are formalized as a Markov Decision Process (MDP).

An MDP is described by a five-element tuple:

1. S: The set of possible states on the ice floor.
2. A: The set of available robot actions.
3. P(s′∣s,a): The probability of transitioning from state s to state s′ upon executing action a.
4. R(s,a,s′): The reward (or penalty) function for the transition.
5. γ∈[0,1): The discount factor for future rewards.

![Место для изображения: ледяная сетка со скольжением 0.8 / 0.1 / 0.1](assets/chapter5.jpg)

## 5.2 Bellman Optimization Equations

The agent's goal in an MDP is to find an optimal policy π∗(s) that prescribes the best action for each state, maximizing the total discounted utility:

```
U(s)=R(s)+γa∈Amaxs′∑P(s′∣s,a)U(s′)
```

This relationship is called the Bellman Equation. It forms the basis of all modern planning systems under uncertainty.

## 5.3 Value Iteration and Policy Iteration

To find the true value of each ice square, ROBO-LUMA launched the iterative Value Iteration algorithm:

```python
def value_iteration(states, actions, P, R, gamma, epsilon=1e-4):
 V = {s: 0.0 for s in states}
 while True:
     delta = 0
     V_new = V.copy()
     for s in states:
         if s.is_terminal:
         continue
         action_values = []
         for a in actions:
             val = sum(P(s_next, s, a) * (R(s, a, s_next) + gamma * 
            V[s_next])
             for s_next in states)
             action_values.append(val)
         V_new[s] = max(action_values)
         delta = max(delta, abs(V_new[s] - V[s]))
     V = V_new
     if delta < epsilon:
     break
 return V
```

Once the iterations converged, the robot extracted the optimal policy:

```
π∗(s)=arga∈Amaxs′∑P(s′∣s,a)V∗(s′)
```

Balancing perfectly on the slippery ledges, the robot guided Mario through the ice dungeon without a single scratch.