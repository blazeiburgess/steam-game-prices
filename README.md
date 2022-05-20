# Steam Prices

Forked from https://github.com/OLoKo64/steam-game-prices

Refactored, removed dependency on selenium, and added a couple features. Some features exist in the original that have not yet been added here.

# Install dependencies

```sh
python3 -m pip install -r requirements.txt
```

# Run

Running with all default options is as simple as:

```
python3 main.py
```

To see what options are available you can see the help message with 

```sh
python3 main.py -h
#or 
python3 main.py --help
```

You have control over the following parameters:

* Operating system (can specify linux, mac, or win)
* Query (arbitrary)
* Tags (must match to steam tags, but will give an error message if not)


To see available tags you can run:

```sh
python3 main.py --list-steam-tags
```

For multiword tags you can use any of the following syntax:

```sh
python3 main.py -t 'open world'
python3 main.py -t 'Open World' # case insensitive
python3 main.py -t open_world # underscores are equivalent to spaces
```

Currently there is no control over what country you are pulling from or the sorting of the final csv. In addition you don't have the ability to open the file from the cli directly. Otherwise functionality should be equivalent.
