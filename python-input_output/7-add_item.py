#!/usr/bin/python3
"""Module: ."""

import sys
from pathlib import Path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

listfile = "add_item.json"

arglist = []

if Path(listfile).exists():
    arglist = load_from_json_file(listfile)

arglist += sys.argv[1:]

save_to_json_file(arglist, listfile)
