# Steam Prices

Forked from https://github.com/OLoKo64/steam-game-prices

Refactored, removed dependency on selenium, and added a couple features. Some features exist in the original that have not yet been added here.

UPDATE 21 May: Add GOG as another store that can be pulled from. This is experimental and doesn't currently allow for different page types (the argument is just ignored). It does support query, tag, offset, and operating system parameters. Differences are: offset is page, not item; tags are different, but can be accessed with the `-s gog --list-tags` arguments.

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

#running for GOG
./bin/run -s gog
```


The equivalent of the 'open world' query below would be

```sh
./bin/run -t open_world # use underscores rather than spaces with docker
```

And a more custom query could be

```sh
./bin/run --page-type newreleases --os linux -t first-person -t puzzle
```

To change country (and implicitly currency) you can use the `--country-code` or `--cc` argument. This accepts case-insensitive iso2 codes or the Enlish version of country names (e.g. "Germany" not "Deutschland", "Brazil" not "Brasil", "China" not "中国").

If you don't know the iso code, you can see it mapped against the english language name with a helper command below

```sh
./bin/run --list-steam-countries # to see a full list

# For Argentina, these are all equivalent and will return ARS$
./bin/run --cc ar
./bin/run --cc Argentina
./bin/run --cc argentina
./bin/run --country-code AR

# For multi-word names underscores are equivalent to spaces, same as tags, e.g.
./bin/run --cc south_africa
./bin/run --cc sierra_leone

# For names with dashes, you can use the dash, e.g.
./bin/run --cc timor-leste
```

I don't know how supported each country is in steam. The countries were just pulled from a list of ISO2 code countries and regions. Also names can be confusing since they came from a list of official names. These can be changed since the ISO code is all that matters.

Examples are:

* "Syrian Arab Republic" not "Syria"
* "Palestinian Territory, Occupied" not "Palestine" 
* "Russian Federation" not "Russia"
* "United Kingdom (Great Britain)" not "United Kingdom"
* "Congo, the democratic republic of the" not "DRC" or "Democratic Republic of the Congo"

Using iso codes is likely the less confusing option.

Again, I have no idea how well any given country is supported. It being in the list is not an indication of anything other than it being listed by the International Organization of Standardization. 

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
#steam tags
python3 main.py --list-tags
#or you can specify steam explicitly
python3 main.py -s steam --list-tags

#gog tags
python3 main.py -s gog --list-tags
```

For multiword tags you can use any of the following syntax:

```sh
python3 main.py -t 'open world'
python3 main.py -t 'Open World' # case insensitive
python3 main.py -t open_world # underscores are equivalent to spaces
```

# TODO

You don't have the ability to open the file from the cli directly. Otherwise functionality should be equivalent with the original repo.

The current sort is on original\_price, discount DESC. So the most expensive gams with the largest discounts will appear at the top. It would be simple to add sorting by columns alone, but some special use cases (e.g. biggest discount by total currency amount, not percentage) would be nice to integrate at the beginning.
