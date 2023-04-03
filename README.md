# timepad
Tool for numpad-like entering of times to control countdown and countdown-to-target of [Clock-8001](https://gitlab.com/clock-8001/clock-8001) via [Companion](https://bitfocus.io/companion).

## Problem to solve
Wanted a numpad on Streamdeck to enter a time which should be used to set a new *countdown from* or *countdown to target* on Clock-8001.
I want to input the time without dividers or placeholder-zeros to reach the correct format.

## What it does
*Timepad* runs as script in the background usually on the same machine as Companion.
It receives an entered number as string from Companion via OSC and interpretes it in a practical way (watch below for details).
For example you can enter just '1' for 1 minute, '130' for 1min 30sec or '030' for 30 seconds.
Then recalculates inputs like 90 minutes to 1 hour, 30 minutes.
Returning the resulting time by changing two custom variables 'timestring' and 'timesecs' in Companion.
This variables can be used in OSC commands for Clock-8001:
'timestring' for countdown to target (format HH:mm:ss)
'timesecs' for countdown from time (seconds)

## Companion config

## Time inputs
