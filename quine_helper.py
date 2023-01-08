#!/usr/bin/env python3

import os
import sys
import time

import git_quine


def deduce_current_contents():
    file_contents = dict()
    for commit in git_quine.get_commits():
        for name, content in commit[2]:
            file_contents[name] = content
    return file_contents


def new_files(restrict_files=None):
    if restrict_files:
        files = restrict_files
    else:
        files = [f for f in os.listdir() if os.path.isfile(f)]
    old_contents = deduce_current_contents()
    new_contents = dict()
    for filename in files:
        with open(filename, 'r') as f:
            new_contents[filename] = f.read()
    new_stuff = []
    for name, new_data in new_contents.items():
        if name == 'git_quine.py':
            lines = new_data.split('\n')
            for i, l in enumerate(lines):
                if l.startswith('REPOSITORY = '):
                    lines[i] = "REPOSITORY = '{}'"
            new_data = '\n'.join(lines)
        elif new_data == old_contents.get(name):
            continue
        print('New contents for ' + name, file=sys.stderr)
        new_stuff.append((name, new_data))
    return new_stuff


def run(argv):
    commits = git_quine.get_commits()
    new_data = new_files(argv[2:])
    assert new_data
    commits.append(('{} +0100'.format(int(time.time())), argv[1], new_data))  # FIXME: Hardcoded timezone
    print('COMMITS:', commits, file=sys.stderr)
    print(git_quine.wrap_commits(commits))


if __name__ == '__main__':
    run(sys.argv)
