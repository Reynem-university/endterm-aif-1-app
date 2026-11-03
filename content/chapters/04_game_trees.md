# Chapter 4. The Castle of Duels — Adversarial Search and Game Trees

## 4.1 Zero-Sum Games and the Minimax Algorithm

At the massive forged gates of the fourth world, the heroes were met by an elite guard — General Koopa. He blocked the tactical bridge and demanded they play a turn-based strategic game on a checkered stone slab.

— This is a classic Zero-Sum Game, — Luigi warned, unfolding the tactical display. — One side's gain is strictly equal to the other side's loss. There is no room for compromise here. Your opponent will calculate your every move just as deeply as you calculate theirs.

The robot built a game tree in its memory where move layers strictly alternate:

- MAX Nodes (ROBO-LUMA): Seek to maximize the position's Utility value.
- MIN Nodes (General Koopa): Seek to minimize the utility for ROBO-LUMA (i.e., maximize their own gain).

The fundamental mathematical definition of the Minimax algorithm is:

```
Minimax(s) = 
  ├── Utility(s),                                      если Terminal(s)
  ├── max { Minimax(Result(s, a)) | a ∈ Actions(s) },  если Player(s) = MAX
  └── min { Minimax(Result(s, a)) | a ∈ Actions(s) },  если Player(s) = MIN
```

## 4.2 Alpha-Beta Pruning Optimization

Mario watched as the robot's processor began sorting through millions of combinations: — At this calculation speed, we'll simply grow old before making our first move!

— Relax, Mario, that's what Alpha-Beta Pruning is for, — Luigi replied. — This method allows us to prune branches of the game tree that are guaranteed to be worse than already found options, sparing us from redundant calculations.

The algorithm maintains two dynamic boundaries:

- α (Alpha): The best (maximum) value guaranteed to the MAX player along the current path.
- β (Beta): The best (minimum) value guaranteed to the MIN player along the current path.

Pruning Rule: if during traversal the condition α≥β is discovered, exploration of that branch terminates immediately because a rational opponent would never allow it to be entered. With optimal move ordering, Alpha-Beta cuts the computational volume in half on an exponential scale (O(bm/2)).

```python
def alphabeta(state, depth, alpha, beta, maximizing_player):
 if depth == 0 or state.is_terminal():
     return state.evaluate_utility()
 if maximizing_player:
     max_eval = float('-inf')
     for child in state.get_successors():
         eval_val = alphabeta(child, depth - 1, alpha, beta, False)
         max_eval = max(max_eval, eval_val)
         alpha = max(alpha, eval_val)
         if beta <= alpha:
             break # Beta cutoff: MIN will never choose this branch
     return max_eval
 else:
     min_eval = float('inf')
     for child in state.get_successors():
         eval_val = alphabeta(child, depth - 1, alpha, beta, True)
         min_eval = min(min_eval, eval_val)
         beta = min(beta, eval_val)
         if beta <= alpha:
             break # Alpha cutoff: MAX will never allow this position
     return min_eval
```

## 4.3 State Evaluation and Depth-Limited Search

Since available battle decision time is limited to milliseconds, ROBO-LUMA cannot calculate the game down to its terminal state. A strict Depth Cutoff is introduced, and the absolute utility function is replaced by a weighted heuristic position evaluation Eval(s):

```
Eval(s)=w1f1(s)+w2f2(s)+⋯+wnfn(s)
```

where fi(s) are key board features (force balance, center control, unit security), and wi are their weight coefficients.

![Место для изображения: оценка позиции на доске](assets/chapter4.jpg)

## 4.4 Expectimax Search and Chance Nodes

Suddenly, General Koopa pulled dice from his pocket and threw them onto the stone slab — an element of chance intervened in the duel's rules. The standard pessimistic Minimax does not work here because it treats the opponent as an absolute villain rather than a generator of random outcomes.

Luigi switched the robot's firmware to Expectimax Search:

- In Chance Nodes, the minimum operation is replaced by calculating the mathematical expectation:

```
V(chance)=s′∑P(s′)⋅V(s′)
```

This allows the agent to weigh risks accounting for the probability of various random events occurring, defeating General Koopa at his own game of chance.
