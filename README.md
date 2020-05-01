Simple Games
============

<!-- vim-markdown-toc GFM -->

* [Overview](#overview)
* [Games](#games)
    * [Naughts and Crosses](#naughts-and-crosses)
    * [Rock, Paper, Scissors](#rock-paper-scissors)
    * [Hangman](#hangman)
    * [Minesweeper](#minesweeper)
    * [Ducks in a row](#ducks-in-a-row)
    * [Towers of Hanoi](#towers-of-hanoi)

<!-- vim-markdown-toc -->

Overview
--------

Due to the current Covid-19 situation I'm stuck in lockdown. The following is
an attempt to write some games something I have never tried before. The games
are all written in Python using only using the standard library. The code here
is very quick and dirty there is a lot of duplication and inelegant code and
there are no tests. The only thing I am doing is using black for formatting
since vim does that for me. This is intentional I wanted to focus on writing
the games and not picking frameworks, writing tests and general code quality.

Games
-----

### Naughts and Crosses

A simple 2 player version of the classic game Naughts and Crosses.

```sh
python3 o_and_x/main.py
```

### Rock, Paper, Scissors

A 0, 1 or 2 player version of Rock, Paper, Scissors, with the option to play
against another human, the AI or watch 2 AIs battle it out.

```sh
python3 rps/main.py
```

### Hangman

Just a quick implementation of the classic word guessing game.

```sh
python3 hangman/main.py
```

### Minesweeper

A text only implemntation of the classic mine hunting game.

```sh
python3 minesweeper/main.py
```

### Ducks in a row

Swap ducks until they are all in a row.

```sh
python3 ducks_in_a_row/main.py
```

### Towers of Hanoi

Basic version of the Towers of Hanoi puzzle.

```sh
python3 tower/main.py
```
