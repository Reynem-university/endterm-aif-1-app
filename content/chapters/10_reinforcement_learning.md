# Chapter 10. The Main Castle — Reinforcement Learning and Defeating Bowser

## 10.1 The Concept of Reinforcement Learning (RL)

The heroes burst into Bowser's main throne room. The giant villain stood on a raised platform, changing his attack tactics lightning-fast: he unleashed a fan of fireballs and launched homing mechanical hammers. Pre-calculated strategy tables and prepared scripts were useless here. Bowser adapted to every move Mario made.

— We need Reinforcement Learning (RL)! — Luigi shouted, switching ROBO-LUMA's core into continuous self-learning mode via trial and error.

Components of the RL environment in the throne room:

- State (s): Robot coordinates, distance to Bowser, phase of the opponent's paw swing.
- Action (a): {Jump,Crouch,Torch Counterattack,Sidestep Dash}.
- Reward (R): +100 for successful evasion and damaging Bowser, −50 for getting hit by a fireball.

![Место для изображения: тронный зал Боузера](assets/chapter10.jpg)

## 10.2 Q-Learning Algorithm and TD Error Equations

The robot employed the model-free Q-Learning algorithm. The Q(s,a) function evaluated the long-term value of executing action a in state s. Weight updates occurred based on the Temporal Difference (TD Error):

```
Q(s,a)←Q(s,a)+α[R+γa′maxQ(s′,a′)−Q(s,a)]
```

where α is the learning rate, and γ is the future reward discount factor.

```python
import numpy as np
class QLearningAgent:
 def __init__(self, num_states, num_actions, alpha=0.1, gamma=0.95, 
epsilon=0.1):
     self.Q = np.zeros((num_states, num_actions))
     self.alpha = alpha
     self.gamma = gamma
     self.epsilon = epsilon
     self.num_actions = num_actions
     def choose_action(self, state):
         # Exploration / Exploitation balance strategy
         if np.random.uniform(0, 1) < self.epsilon:
             return np.random.choice(self.num_actions) # Exploration
         return np.argmax(self.Q[state, :]) # Exploitation
     def update(self, state, action, reward, next_state):
         best_next_action = np.argmax(self.Q[next_state, :])
         td_target = reward + self.gamma * self.Q[next_state, best_next_action]
         td_error = td_target - self.Q[state, action]
         self.Q[state, action] += self.alpha * td_error
```

## 10.3 Balancing Exploration and Exploitation (ϵ-greedy)

To avoid getting stuck in the first successful evasion strategy, the robot used the ϵ-greedy strategy:

- With probability ϵ, the robot performed a random action (Exploration), trying out new non-standard counterattacks.
- With probability 1−ϵ, the robot chose the proven optimal action from the Q(s,a) table (Exploitation).

As combat episodes progressed, the parameter ϵ smoothly decreased from 1.0 to 0.01, turning the robot into a flawless master of tactical combat.

## 10.4 Epilogue: Rescuing Princess Peach and the AI Expert Diploma

At the 500th training episode, ROBO-LUMA's Q(s,a) table converged to the global optimum.

The robot's movements became indistinguishable from a dance: calculating trajectories with jewel-like precision, ROBO-LUMA executed a flawless jump, dodged a wall of flame, delivered a lightning-fast combo strike to a vulnerable armor joint of Bowser, and extended its manipulator toward a hidden wall lever.

Clack!

The mechanical lock snapped open with a roar, and the bridge beneath Bowser's feet dropped straight into the boiling lava. The villain vanished into the fiery abyss with a scream. The transparent force field over the center of the throne room dissipated, and a safe and sound Princess Peach stepped onto the platform.

With tears of joy in her eyes, the princess hugged Mario and thanked the brilliant engineer Luigi for creating such a flawless autonomous system. In recognition of these achievements, Peach personally presented Mario and his faithful robot ROBO-LUMA with a golden AI Expert Diploma, certifying the successful mastery of all fundamental algorithms of modern data science.

The Mushroom Kingdom was saved — this time by pure mathematics, rigorous logic, and flawless algorithms.

![Место для изображения: финал, диплом AI Expert](assets/chapter10_2.jpg)