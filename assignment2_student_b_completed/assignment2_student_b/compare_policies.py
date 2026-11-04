"""Find action changes between learned policies with matching experiment settings.

AI disclosure: Drafted with OpenAI ChatGPT (GPT-6) 2026-11-04.
Add the conversation share URL in final submitted files.
"""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('policy_high_p', type=Path)
    parser.add_argument('policy_low_p', type=Path)
    parser.add_argument('--output', type=Path, default=Path('changed_actions.csv'))
    args = parser.parse_args()
    first = json.loads(args.policy_high_p.read_text(encoding='utf-8'))
    second = json.loads(args.policy_low_p.read_text(encoding='utf-8'))
    shared = sorted(first.keys() & second.keys())
    changed = [(s, first[s], second[s]) for s in shared if first[s] != second[s]]
    import csv
    with args.output.open('w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(['state', 'action_high_p', 'action_low_p'])
        writer.writerows(changed)
    print(f'{len(changed)} action changes among {len(shared)} states visited in both training runs.')
    if changed:
        print('Example candidate:', changed[0])
    print('Confirm state visitation counts and reproducibility before reporting a change.')


if __name__ == '__main__':
    main()
