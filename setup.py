#!/usr/bin/env python
"""setup.py writes an environment file for this project.

Run "python setup.py -h" to see the required arguments.
"""
import argparse
from os import environ
import jinja2
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--destination', default='.environment',
        help='Location of environment file to write to. Defaults to ".environment"')
parser.add_argument('-m', '--meetup-api-key', required=True)
parser.add_argument('-a', '--activate-base-conda',
        help='Full path to base conda activate script.')
parser.add_argument('-n', '--conda-env-name')
parser.add_argument('-q', '--quiet', action='store_true')
args = parser.parse_args()
template = jinja2.Template(open('environment.j2', 'r').read())
with open(args.destination, 'w') as f:
    f.write(template.render(vars(args)))
if not args.quiet:
    print(f"Created {args.destination}.")
