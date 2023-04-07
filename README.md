# pyGoL
CLI Game of Life to fill your terminal windows. written in python.

# Installation

Get the latest version of [python](https://www.python.org/).

Save `gol.py` to your machine.

## Windows

You are done.

## Linux

Add the shebang `#!/usr/bin/env python` to the top of the file.

Make the file executable:
```
chmod u+x gol.py
```

Optionally,
place it in your `bin` folder and remove the `.py` extension to cleanly run it anywhere:
```
sudo cp gol.py /usr/bin/gol
```

# Usage
double click it or run it from a terminal window

```
-rs RULESET, --rule-set RULESET
                Defining game of life ruleset. Default: 'default' (original b3s23 game)
-g GENERATIONS, --generations GENERATIONS
                Maximum number of generations before ending a game of life. -1 for an infinite game. Default: 500

-d DELAY, --delay DELAY
                Number of seconds between iterations. Default: 0.1125
```

## Rulesets

Rulesets are defined by the conditions for a cell to be born or to survive. THe original ruleset proposed by Conway consisted of birth when surrounded by 3 living cells and survival while surrounded by 2 or 3 living cells.

Effective shorthand: B3/S23

Below are the different rulesets that can be fed as arguments to the program using the `-rs` flag
|Ruleset name(s)|rules|description|
|:-|:-|:-|
|` ` `default`|B3/S23|classic|
|`replicator`|B1357/S1357|every pattern turns into a [replicator](https://conwaylife.com/wiki/Replicator)|
|`seeds`|B2/S|explodes under completely random grid, can be fed patterns that result in interesting and simple [spaceships](https://conwaylife.com/wiki/Spaceship)|
|`blank` `kuhaku`|B25/S4|I don't remember where I found this|
|`life-without-death` `LWD` `inkspots` `flakes`|B3/S123456789|very cool :)|
|`34` `34-life` `34L`|B34/S34|explosive with simple spaceships|
|`diamoeba`|B35678/S5678|makes big diamonds|
|`block` `2x2`|B36/S125|many simple [still lifes](https://conwaylife.com/wiki/Still_life), [oscillators](https://conwaylife.com/wiki/Oscillator), spaceships, and 2x2 blocks|
|`morley` `move`|B368/S245|lots of simple oscilators and stabilizes randomness very quickly|
|`majority` `vote`|B34678/S35678|stabilizes into blobs|
|`anneal` `twisted-majority-rule` `TMR`|B5678/S45678|modification of the previous, does not stabilize|

Different rulesets are defined in code underneath the `ruleCheck()` function using an elif ladder and primitive integer arrays.

The design is very human making it easy to edit and expand upon. The [there's a lot of different rules](https://conwaylife.com/wiki/List_of_Life-like_rules) that you can choose to implement if you so choose. I'm a big fan of `anneal` myself :).

# TODO

 - [ ] Accept input from a file
 - [ ] Output final gamestate to files
 - [ ] Make forever looping optional
 - [ ] Implement more rulesets
