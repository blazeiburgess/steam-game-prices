# Steam Prices

Forked from https://github.com/OLoKo64/steam-game-prices

Refactored, removed dependency on selenium, and added a couple features. Some features exist in the original that have not yet been added here.


# Run

## Docker

The `./bin/build` and `./bin/run` files use docker-compose to execute. 

### Install dependencies

Building or rebuilding the image is

```sh
./bin/build
```
### Executing the application


A more full list of commands are below, but basic running with default parameters is just:

```sh
./bin/run # on first run this should build, but any changes will have to be rebuilt
```


The equivalent of the 'open world' query below would be

```sh
./bin/run -t 'open world'
```

And a more custom query could be

```sh
./bin/run --page-type newreleases --os linux -t first-person -t puzzle
```

## Direct

### Install dependencies

It may make sense to setup a virtual environment:

```sh
python3 -m virtualenv venv
. venv/bin/activate
```

In any case, installing dependencies will involve

```sh
python3 -m pip install -r requirements.txt
```

### Executing the application

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

The current sort is on original\_price, discount DESC. So the most expensive gams with the largest discounts will appear at the top.
