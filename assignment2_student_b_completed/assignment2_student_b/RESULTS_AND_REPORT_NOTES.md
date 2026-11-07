# Verified corrected Q-Learning results and report integration

These results were generated **after** fixing state initialization and changing the state to the **five-component** `(row, col, has_package, delivered, steps_remaining)` form from the group `Assignment2_Report.docx`. They supersede the earlier four-component Q-Learning report table.

## Experimental setup

- Instructor's original 10×10 warehouse; station layout seed 42.
- Separate adapter samples intended action probability p, with each perpendicular action at `(1-p)/2`, and delegates all collision/reward handling to instructor `step`.
- 120-step cap; feasible progress phases `(0,0)`, `(1,0)`, `(1,1)`; states explicitly initialized for each time remaining value 0..120.
- Two configurations: A `(alpha=.20, gamma=.95, epsilon decay=.995)`; B `(alpha=.10, gamma=.99, epsilon decay=.999)`; epsilon start 1, floor .05.
- p in 1.00, .90, .80; random training seeds 11, 42, 99; 5000 episodes per combination; 100 *independent motion-seeded* epsilon-zero evaluation episodes per trained policy.
- 18 trained policies, 90,000 training episodes and 1,800 evaluation episodes.

## Results (300 greedy evaluations per row)

| Configuration | p | Mean cumulative reward | Success rate | Mean steps |
|---|---:|---:|---:|---:|
| A | 1.00 | 137.00 | 100.00% | 26.00 |
| A | 0.90 | 107.00 | 98.00% | 37.92 |
| A | 0.80 | 52.05 | 88.67% | 54.91 |
| B | 1.00 | 137.00 | 100.00% | 27.00 |
| B | 0.90 | 106.84 | 96.67% | 38.02 |
| B | 0.80 | -66.46 | 49.00% | 87.94 |

## Interpretation and limitations

- The 5-field representation matches the report, but dramatically enlarges the set of Q states. One physical location/task phase has separate values for every number of steps remaining; data is spread across more distinct states. This is why the corrected runs are *not* directly interchangeable with earlier 4-field results.
- Lower p makes control less reliable, raises the expected number of steps, and decreases rewards. Configuration B performs particularly poorly at p=.80 within the 5000-episode budget; do not claim both configurations achieve 100% success.
- A p=1.00 still has successful greedy policies with 24–28 steps depending on training configuration/seed; their reward is below the reported 143.00 Value Iteration result, so 5000 episodes have not produced equivalent deterministic efficiency.
- `policy_grid.png` shows *visited-state arrows* only for p=1, .9, .8 at three labelled time slices. `sample_routes.png` is one stochastic evaluation trajectory per p. Neither plot proves universal policy optimality.
- `changed_actions.csv` compares Q policies at p=1.00 and p=.80 for A/seed11; visit counts >=20 in both states are required. State visitation alone does not guarantee convergence or per-action exploration; use the `action_visits_*.json` diagnostics and compare several seeds before selecting a change to describe.
- VI rewards and iteration counts in the group DOCX are *reported by Student A*, not independently verified here. Different evaluation seed sets and episode counts prevent a fully paired head-to-head claim. Align rollout seeds and identical horizon, or explicitly state the comparison is descriptive.
- Include actual code/chat source links in the AI use disclosure; the available text still has placeholders.

## Report changes

- **Section 4.1**: report explicit zero Q-table with 27,951 valid time-aware states x four actions, the update, epsilon greedy, terminal bootstrap zero, and epsilon schedule.
- **Section 4.2**: give A and B hyperparameters and seeds 11, 42, 99; explain 18 independent configurations.
- **Section 4.3**: use `training_reward.png`, `training_success.png`, and the *new* evaluation performance table; describe approximate improvement without claiming guaranteed convergence.
- **Section 4.4**: include `policy_grid.png` and a concrete `example_greedy_run_*.csv`, explaining epsilon=0 and no Q updates.
- **Section 5.3**: replace the old Q-Learning averages with the six new rows above.
- **Section 5.4/6.1–6.3**: comparison with VI from the group report is descriptive until evaluation episodes are paired; note configuration A uses the same gamma .95 and B .99 is a hyperparameter sensitivity run.
- **Section 5.5**: do not confuse Student A's five-component example `(5,1,1,1,96)` with the four-component examples from the old Q-Learning code. New Q policies use five-component states.
