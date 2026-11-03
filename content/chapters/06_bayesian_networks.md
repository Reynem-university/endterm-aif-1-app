# Chapter 6. Misty Swamps — Probabilistic Inference and Bayesian Networks

## 6.1 Bayes' Theorem Under Uncertainty

Thick vapors and toxic mud in World 6 completely knocked out the robot's optical cameras. Sensors recorded strange sounds and rustles, but the noise level exceeded permissible limits. Mario listened closely to the bubbling mud: — Someone's out there! Is it an enemy or just a bursting gas bubble?

Luigi tuned the processor for probabilistic analysis using Bayes' Theorem:

```
P(Koopa Splash)= ∣ P(Splash)P(Splash Koopa)⋅ ∣ P(Koopa)
```

where:

- P(Koopa) is the prior probability of finding an adversary in the swamp.
- P(Splash Koopa) is the Likelihood function. ∣
- P(Koopa Splash) is the desired posterior probability (Degree of Belief) after receiving an acoustic ∣ cue.

![Место для изображения: болото и теорема Байеса](assets/chapter6.jpg)

## 6.2 Bayesian Belief Networks

To combine data streams from ultrasonic rangefinders, temperature sensors, and the acoustic locator, ROBO-LUMA built a Bayesian Network — a Directed Acyclic Graph (DAG) where nodes represent random variables and edges encode conditional dependencies.

Example network structure for a swamp post:

```
 [ Drought (D) ]
 / \
 v v
 [ Swamp (M) ] [ Reed (R) ]
 \ /
 v v
 [ Sensor Rustle (S) ]
```

Each network node is backed by a Conditional Probability Table (CPT). The joint probability distribution of the entire system is expressed as the product of local conditional probabilities:

```
P(X1,X2,…,Xn)=i=1∏nP(Xi∣Parents(Xi))
```

This allows the robot to calculate precise risks even when half of its sensor modules fail.
