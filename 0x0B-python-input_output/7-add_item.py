#!/usr/bin/python3
""" The "7-add_item" Module
A script that adds all arguments to a Python list,
and then save them to a file
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except Exception:
    json_list = []

for i in sys.argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, filename)
