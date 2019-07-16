# git_quine

> A program that recreates its own repository

Why?  Because, that's why!

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)

## Install

How do you mean?  It's a quine.  It produces itself as output.
There is nothing to install.

## Motivation

> Bäärenkatapult!  "Warum?"  Fick Dich! Deshalb!

## Usage

Just run it!  It should produce exactly the same commits on every platform.

```
$ ls -a
.git .gitignore git_quine.py  LICENSE  README.md
$ ./git_quine.py
Git repository created in git_quine/
$ ls git_quine/
.git .gitignore git_quine.py  LICENSE  README.md
$ diff -su <(git rev-parse HEAD) <(git -C git_quine/ rev-parse HEAD)
Files /dev/fd/63 and /dev/fd/62 are identical
```

### Stand-alone

To prove that it doesn't just copy the files, I encourage you to take `git_quine.py`,
move it somewhere else, delete the repository, and run the quine.
You will see that it reproduces the entire repository *without* access to anything else.

### Feature support

This quine supports arbitrary commit messages and times, added files, and changes to files.

Naturally, it can't reproduce *all* features of git.  Most importantly,
this quine currently only understands history as a single branch, consisting only of single-parent commits.
Also, this quine is its own author *and* committer, because that simplifies things.

Diffs are stored inefficiently.

If you take a deep dive into how this quine works, you will see that these missing features can be easily added.

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/git_quine/issues/new) or submit PRs.
