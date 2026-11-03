# Chapter 8. Crossing the Lava River — Rational Decisions and Utility Theory

## 8.1 Maximum Expected Utility (MEU)

Before the heroes spread a boiling river of molten lava. Three ancient bridges crossed it, but their load-bearing structures were compromised. Falling into the lava meant total destruction of the robot.

Luigi activated the rational choice module based on the principle of Maximum Expected Utility (MEU). The expected utility of action a given current observations e is calculated as:

```
EU(a∣e)=s′∑P(Result(a)=s′∣a,e)⋅U(s′)
```

A rational agent chooses the action that yields the highest mathematical expectation of utility:

```
a∗=argamaxEU(a∣e)
```

![Место для изображения: три моста через лавовую реку](assets/chapter8.jpg)

## 8.2 Loss Function and Error Costs (Loss Units)

Mario pointed to a series of suspicious doors leading into the bridge towers: — Should we blast through all of them with the torch right now?

Luigi opened the Loss Matrix on the screen:

| Actual State / Agent Action | Consider Safe (Action 1) | Attack with Torch (Action 2) |
|-----------------------------|--------------------------|------------------------------|
| Door is safe                | Loss=0                   | Loss=10 (Property damage)    |
| Enemy is hiding behind door | Loss=100 (Ambush death)  | Loss=2 (Fuel consumption)    |

Due to the colossal cost of a False Negative error (Loss=100), the rational decision threshold shifts: the robot opens preemptive torch fire even at the slightest probability of an ambush presence (P(Enemy)>0.09).
