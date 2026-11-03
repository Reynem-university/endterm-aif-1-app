# Chapter 7. Tracking the Invisible Bowser — Hidden Markov Models (HMM)

## 7.1 Hidden States and the Emission Matrix

Bowser deployed an experimental quantum invisibility field. His physical coordinates inside the multi-level castle became a hidden state (Xt), inaccessible to the robot's direct scanners. ROBO-LUMA recorded only indirect signs: floor tile vibrations and air temperature fluctuations (observations Et).

To model such systems, a Hidden Markov Model (HMM) is used, defined by three parameters:

1. Initial probability distribution π=P(X1).
2. State transition probability matrix Tij=P(Xt=sj∣Xt−1=si).
3. Emission (observation) matrix Ejk=P(Et=ok∣Xt=sj).

## 7.2 Core HMM Tasks and the Viterbi Algorithm

The robot performs three types of logical inference in an HMM:

- Filtering: Calculating the current probability distribution of hidden states given the entire history of observations P(Xt∣e1:t).
- Smoothing: Refining the enemy's past coordinates accounting for new evidence P(Xk∣e1:t), where k<t.
- Viterbi Decoding: Finding the single most probable trajectory of the invisible Bowser's movement through the castle.

```python
import numpy as np
def viterbi(obs, states, start_p, trans_p, emit_p):
 V = [{}]
 path = {}
 # Initialization for t = 0
 for st in states:
     V[0][st] = start_p[st] * emit_p[st][obs[0]]
     path[st] = [st]
 # Dynamic programming for t > 0
 for t in range(1, len(obs)):
     V.append({})
     newpath = {}
     for st in states:
         (prob, state) = max(
         (V[t-1][st0] * trans_p[st0][st] * emit_p[st][obs[t]], st0)
         for st0 in states
         )
         V[t][st] = prob
         newpath[st] = path[state] + [st]
     path = newpath
 (prob, state) = max((V[len(obs) - 1][st], st) for st in states)
 return prob, path[state]
```

By running the Viterbi algorithm over floor vibration logs, ROBO-LUMA predicted Bowser's exit point from the masking zone with meter-level accuracy.

![Место для изображения: траектория Боузера по алгоритму Витерби](assets/chapter7.jpg)