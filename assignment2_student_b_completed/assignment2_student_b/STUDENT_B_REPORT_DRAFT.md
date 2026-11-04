# Student B — Q-Learning Implementation and Experiments

**Status:** Draft for integration into the group PDF. Text about methodology is ready; all empirical values in brackets must be filled from **real runs of the provided `gridworld_domain`**. No numerical experimental outcomes are claimed here.

## Part 2: Reinforcement Learning — Q-Learning

### State and action representation

The robot must pick up a package, deliver it to the packing station, and return to its charging dock. The state must encode both location and progress. We use the same state definition as Part 1: `(x, y, phase)`, with phase 0 before pickup, phase 1 while carrying, and phase 2 after delivery, subject to alignment with the teammate's final MDP representation. Coordinates alone cannot distinguish whether the robot may earn a pickup, delivery, or return reward. The robot chooses from the four movement actions: up, down, left, and right. The Q-table initially contains zero for every state-action pair; a dictionary initializes entries on first access. Under a known fixed 10×10 map, this is equivalent to zero initialization of the required entries, but entries in never-visited states remain untrained.

### Q-Learning update

For the current state `s`, selected action `a`, received reward `r`, and observed next state `s'`, we use the one-step update:

`Q(s,a) <- Q(s,a) + alpha * [r + gamma * max_a' Q(s',a') - Q(s,a)]`.

For a terminal transition, the future-value term is zero. The learning rate `alpha` determines the size of each update, while `gamma` discounts future rewards. Unlike Value Iteration, this algorithm uses sampled experiences and is not given the transition probabilities. The environment implements the motion uncertainty, including sideways movement and blocked actions; the agent only sees the resulting next state and immediate reward.

### Exploration and training

The training policy uses epsilon-greedy exploration. With probability epsilon the agent selects an action uniformly at random. Otherwise, it selects an action with the largest available Q-value, breaking ties randomly. Epsilon begins at 1.0, decreases after each episode, and is not allowed below 0.05. We train for [ACTUAL NUMBER] episodes for each configuration, motion probability, and random seed. Each episode ends when the task finishes or reaches the environment step limit. We record cumulative episode reward, completion success, total steps, and epsilon.

### Hyperparameter configurations

| Configuration | Learning rate alpha | Discount gamma | Epsilon start | Epsilon decay | Epsilon minimum |
|---|---:|---:|---:|---:|---:|
| A, fast decay | 0.20 | 0.95 | 1.00 | 0.995 | 0.05 |
| B, slow decay | 0.10 | 0.99 | 1.00 | 0.999 | 0.05 |

These are preliminary choices, not preset values in the assignment. Changes in outcomes cannot be attributed to one hyperparameter because the configurations change alpha, gamma, and decay simultaneously.

### Random seeds and evaluation

The planned seeds are 11, 42, and 99. For each configuration, we evaluate its learned greedy policy without exploration or learning updates. Evaluation episodes use separate seeds from training. The planned evaluation count is 100 episodes per trained policy. Success means the robot picked up the package, delivered it, and returned to the charging dock before reaching the step limit. We calculate the mean cumulative reward, success rate, and mean episode length for each configuration and seed.

### Training and convergence results

**Insert the generated `training_reward.png` and `training_success.png` after the code is connected to the actual Gridworld.**

In the final version, describe the approximate episode range at which the smoothed reward and success curves stabilize. Distinguish an apparent plateau from proof of convergence and report the variability across seeds. Record [OBSERVED REWARD TREND], [OBSERVED SUCCESS TREND], and [OBSERVED SEED VARIABILITY].

### Greedy policy and example run

After training, the greedy policy selects `argmax_a Q(s,a)` for each learned state. During evaluation, exploration is disabled (epsilon=0). Include one actual evaluation trace with start state, pickup event, delivery event, return event, total reward, and number of steps. A policy arrow figure should indicate which task phase is displayed; different phases can require different preferred directions at the same grid cell. [INSERT VERIFIED EXAMPLE RUN AND POLICY FIGURE.]

## Part 3: Stochastic Motion and Q-Learning

### Experimental setup

The intended action is executed with probability `p`; the remaining probability `1-p` is divided equally between the two perpendicular actions. We evaluate `p=1.00`, `p=0.90`, and `p=0.80`. The `p=0.80` setting is the baseline shared with Parts 1 and 2. For every `p`, train Q-Learning separately, use identical evaluation settings, and retain the same grid layout and task rules. The agent receives observations from the environment and is not given `p` as input.

### Results table (fill only after actual execution)

| Intended-action probability | Configuration | Mean evaluation reward | Evaluation success rate | Approx. stabilization episode |
|---|---|---|---|---|
| 1.00 | A | [result] | [result] | [result] |
| 0.90 | A | [result] | [result] | [result] |
| 0.80 | A | [result] | [result] | [result] |
| 1.00 | B | [result] | [result] | [result] |
| 0.90 | B | [result] | [result] | [result] |
| 0.80 | B | [result] | [result] | [result] |

Report per-seed results or variation as well as the means. The robot may prefer safer routes when action uncertainty increases, especially near shelves or congestion penalties, but this is a hypothesis to check with the learned policies rather than an observed result. Identify a concrete state `(x, y, phase)` where the greedy action differs across `p`, verify it was adequately visited during training, and explain how sideways motion changes its expected consequences. [INSERT VERIFIED STATE AND ACTIONS.]

### Comparison with Value Iteration (joint work)

Compare Q-Learning and Value Iteration under the **same** action probabilities, map, rewards, discount factor where possible, step limit, and evaluation seeds. Include average cumulative reward, success rate, learning/convergence behaviour, and phase-specific policy differences. The Value Iteration algorithm uses the known transition and reward model; Q-Learning estimates action values from experience. Whether they find the same routes must be established from the outputs rather than assumed. [INSERT STUDENT A'S VI RESULTS AND JOINT COMPARISON.]

### Limitations

The number of episodes, epsilon schedule, and selected random seeds may affect the result. A Q-table can remain inaccurate in rarely visited states. Reported apparent convergence depends on chosen smoothing and evaluation windows. Evaluations based on one warehouse layout do not establish general performance on other layouts. If a state remains unvisited or underexplored, its displayed greedy action should not be treated as a validated policy decision.

### Group contribution statement

Student B implemented and analyzed Q-Learning in Part 2 and its motion-uncertainty experiments in Part 3. Student A handled MDP formulation and Value Iteration. Both students jointly compare the results and prepare the final submission. Adjust this statement to match work actually completed.

### Generative AI disclosure

OpenAI ChatGPT (GPT-6) was used on November 4, 2026, to draft initial Q-Learning code, experimental organization, and report prose based on the supplied assignment and the team division image. We reviewed and validated the work against the course-provided Gridworld before submission. **Shared prompt/conversation link: [INSERT ACTUAL SHARE URL].** Remove the validation claim if verification has not yet occurred.
