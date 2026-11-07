"""Small reproducibility tests for Student B's Q-Learning code."""
import random
from q_learning import QAgent, Settings, train, evaluate
from warehouse_bridge import create_env


def run_tests():
    env = create_env(p=0.8, max_steps=120)
    state = env.reset(seed=11)
    assert len(state) == 5 and state[-1] == 120, state
    agent = QAgent(env.actions, alpha=0.2, gamma=0.95)
    agent.initialize_states(env)
    assert len(agent.q) == 27951, len(agent.q)
    assert len(agent.q[state]) == 4
    for action in env.actions:
        ns, reward, term, trunc = env.step(action)
        assert len(ns) == 5
        assert ns[-1] == 119
        env.reset(11)
    s = (6, 0, 0, 0, 120)
    sn = (6, 0, 0, 0, 119)
    agent.update(s, 0, 10.0, sn, True)
    assert abs(agent.q[s][0] - 2.0) < 1e-10
    agent2, history = train(create_env, Settings('test',0.2,0.95,0.995), 11, 4, 0.8, 120)
    assert len(history) == 4
    outcome, path = evaluate(create_env, agent2, .8, 11, 2, 120)
    assert len(outcome) == 2 and path[0]['step'] == 0
    print('PASS: state, Q-table, stochastic wrapper, Bellman update, training and greedy evaluation')

if __name__ == '__main__':
    run_tests()
