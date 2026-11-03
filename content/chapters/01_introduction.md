# Chapter 1. The Birth of ROBO-LUMA and the AI Legal Compass

![Место для изображения: обложка главы 1](assets/cover.png)

## 1.1 PEAS Architecture and the Perception-Action Loop

The Toad Town Castle met the heroes with the echoing silence of empty corridors and the flicker of holographic displays on the training grounds. Luigi carefully lowered ROBO-LUMA's chassis onto the metal floor tiles, connected a diagnostic cable to the port on the robot's chest panel, and flipped the main toggle switch.

— Look, Mario, — Luigi began, watching cascades of pixels come alive on the robot's external screens. — Artificial intelligence is not born as a ready, all-knowing deity. Any autonomous system, whether a simple thermostat or a space probe, is built upon the fundamental Agent-Environment Loop paradigm.

Luigi waved his hand, summoning a holographic diagram in the air:

```
 +------------------+
 | Environment |
 +------------------+
 | ^
 Sensors | | Actuators
 v |
 +------------------+
 | Agent (AI) |
 +------------------+
```

![Место для изображения: диаграмма Agent-Environment Loop](assets/chapter1.jpg)

- Agent: An entity that perceives its environment through sensors and acts upon it through actuators. In our case, the agent is ROBO-LUMA.
- Environment: The external world in which the agent exists, makes decisions, and commits errors.

To design an agent without "blind spots" in its technical specification, engineers use the PEAS framework:

| PEAS Component      | Description in the Context of the Mushroom Kingdom                                                                                    |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Performance Measure | Maximizing the probability of rescuing Princess Peach, minimizing robot damage, conserving battery power, and collecting bonus coins. |
| Environment         | The Mushroom Kingdom: dynamic platforms, moving enemies (Goombas, Koopas), lava lakes, changing weather conditions, and obstacles.    |
| Actuators           | Hydraulic jumping platforms, wheel-track drive, manipulator arm for object handling, and torch emitter.                               |
| Sensors             | Stereo-vision optical cameras, ultrasonic rangefinders, LiDARs, gyroscope, lava temperature sensor, and audio locator.                |

## 1.2 Rationality in the Mushroom Kingdom

Mario crossed his arms, skeptically eyeing the blinking LEDs on the robot's head: — So now this metal box is going to act flawlessly? If it's so smart, let it tell us right away which of the ten castles Bowser is hiding in so we don't waste time running through swamps!

Luigi smiled condescendingly and shook his head: — That is the misconception of beginners, Mario. A rational agent is not an omniscient agent. Omniscience requires absolute knowledge of the future, but in the real world, this is mathematically impossible due to environmental stochasticity.

Luigi folded his fingers, listing the four pillars of rationality:

1. A performance measure that defines the criterion of success.
2. The agent's prior knowledge about the environment.
3. The actions that the agent can perform.
4. The agent's percept sequence (history of perceptions) from launch up to the current time step.

Definition of Rationality: A rational action is an action that maximizes the expected performance measure based on the information available at the time, rather than absolute actual success in the future. If a robot made a logically sound decision based on all available data, but unexpectedly ran into a hidden mine, its action was still entirely rational.

## 1.3 Legal Framework and AI Safety

Before activating the navigation module for the first world, Luigi opened a secure root directory in the console and loaded a legal block into the robot's RAM.

— We are operating within a legal framework, Mario, — the engineer said sternly as he entered the master password. — In accordance with the Republic of Kazakhstan Law No. 230-VIII ZRK "On Artificial Intelligence," any autonomous system must function strictly within the bounds of rigorous ethical and legal standards. We cannot allow the robot to destroy castle infrastructure or harm peaceful citizens.

Luigi initiated the compilation of seven core safety principles into ROBO-LUMA's neural network core:

- Human Priority and Safety: The life and health of Mario, Princess Peach, and the peaceful residents of the Mushroom Kingdom always take absolute precedence over any tactical mission objectives.
- Legality and Fairness: The robot's algorithms must not discriminate against peaceful inhabitants of the kingdom or violate local laws.
- Transparency and Explainability: Upon any request from an engineer, the robot must provide a clear log report justifying the reasons for choosing a particular maneuver.
- Risk Classification: All tasks performed by the robot are divided into three categories:
  - Minimal risk: Routine navigation across open fields and coin collection.
  - Medium risk: Maneuvering near precipices and labyrinths.
  - High risk: Activating the torch emitter or combat systems near residential buildings.
- Synthetic Content Marking: Any holograms, messages, or audio signals generated by the robot's artificial intelligence must carry a digital label reading "Generated by AI."

Having completed the setup, Luigi pressed the enter key. ROBO-LUMA's body swayed smoothly on its tracks, a green readiness indicator lit up on the main screen, and a fog-shrouded path leading into the depths of World 2 opened up before the heroes.
