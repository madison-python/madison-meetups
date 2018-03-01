# Meetups in Madison, WI

## Installation

First clone this repository to your local machine via

```bash
$ git clone https://github.com/madison-python/madison-meetups.git
$ cd madison-meetups
```

A `conda` environment with the necessary dependencies for this project can be created via:

```bash
$ conda env create --file environment.yml
$ source activate madison-meetups
```

Note, if `conda` is not installed on your machine, see the [miniconda installation guide](https://conda.io/docs/user-guide/install/index.html).

## Setup

In order to use the [`meetup-api`](https://github.com/pferate/meetup-api) Python package,
you must have a `MEETUP_API_KEY` environment variable set. This can be done via:

```bash
$ export MEETUP_API_KEY=my_special_api_key_value
```

See https://secure.meetup.com/meetup_api/key/ for getting an API key. 
