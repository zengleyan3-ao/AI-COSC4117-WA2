# COSC-4117EL Assignment 2 — Student B (Q-Learning)

This is an executable Q-Learning package using the **professor-provided** `warehouse_gridworld_domain_random.py`, with one documented stochastic adapter. It does not use a replacement simulator.  
**AI use disclosure:** ChatGPT GPT-6 helped create and test the code and report on 2026-11-06. 

## Files

- `warehouse_gridworld_domain_random.py`: copied instructor environment. **Only alteration**: `import pygame` is guarded with `try/except ImportError` so headless experiments run without optional GUI software. Original numerical logic is otherwise unchanged; interactive visualization still requires pygame.
- `warehouse_bridge.py`: wrapper around the original environment. Samples intended action with probability `p`; samples either perpendicular with `(1-p)/2`; executes original `world.step(executed_action)` so rewards, shelving, congestion, and flags remain instructor-defined. Fixed layout seed 42, separate motion RNG, `max_steps=120`.
- `q_learning.py`: table-based Q-Learning, two hyperparameter settings, three seeds, training, greedy evaluation and plots.
- `plot_policies.py`: staged policy grid and example sampled rollout plot.
- `compare_policies.py`: find differing learned policy actions for two settings.
- `STUDENT_B_REPORT.md`: complete Student B numerical report, leaving the VI comparison for team integration.
- `STUDENT_B_REPORT.pdf`: printable report.
- `results_q_learning/`: full numeric CSVs, policies, visitation-count JSONs, example greedy runs and PNG charts.

## Requirements

Python 3.10+; `numpy`, `matplotlib`. `pygame` is optional for training and policy plots but needed for the original interactive GUI. No Gymnasium.

## Reproduce training / evaluation

Run from **this directory**:

```bash
python q_learning.py --episodes 5000 --eval-episodes 100 --max-steps 120 --seeds 11 42 99 --probabilities 1.0 0.9 0.8 --output results_q_learning
python plot_policies.py
python compare_policies.py results_q_learning/policy_A_fast_decay_p1.00_seed11.json results_q_learning/policy_A_fast_decay_p0.80_seed11.json --output results_q_learning/changed_actions.csv
```

**Fixed warehouse positions (row, col):** pickup `(2,2)`, packing `(0,4)`, charging dock `(6,0)` from layout seed 42. Training seeds 11, 42, 99 affect motion/exploration, not the layout. All three task phases use the framework-provided four-field Markov state `(row,col,has_package,delivered)`. Action space retains invalid commands as in the original framework. The Q agent is never passed `p`; only the environment adapter is configured with it.


