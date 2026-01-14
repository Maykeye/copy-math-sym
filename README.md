# copy-math-sym

KISS script to select a math symbol and copy them into the (wayland) clipboard using python, wofi and wl-copy

## Usage

Run: `python copy-math-sym.py [<category>]` 

where category is based on unicode category and one of:

* letters
* numbers
* operators
* arrows
* misc (also misc-a, misc-b, misc-op)
* sup
* alnum

`misc` mixes all `misc-a`, `misc-b`, `misc-c`

## Requirements (must be in `$PATH`):

* wofi
* wl-copy

## Example of integrating in niri

```~/config/niri/config.kdl
...
binds {
    Mod+F1 { spawn  "sh" "-c" "python ~/scripts/copy-math-sym.py operators"; }
    Mod+F2 { spawn  "sh" "-c" "python ~/scripts/copy-math-sym.py numbers"; }
    Mod+F3 { spawn  "sh" "-c" "python ~/scripts/copy-math-sym.py letters"; }
    Mod+F4 { spawn  "sh" "-c" "python ~/scripts/copy-math-sym.py arrows"; }
}
...
```
(`sh -c` is used to resolve `~`)