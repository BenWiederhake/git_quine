# git-quine

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
.git .gitignore git-quine.py  LICENSE  README.md
$ ./git-quine.py
Git repository created in git-quine/
$ ls git-quine/
.git .gitignore git-quine.py  LICENSE  README.md
$ diff -su <(git rev-parse HEAD) <(git -C git-quine/ rev-parse HEAD)
Files /dev/fd/63 and /dev/fd/62 are identical
```

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/git-quine/issues/new) or submit PRs.
