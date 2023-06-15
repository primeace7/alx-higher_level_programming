#!/usr/bin/python3

'''
Define a fuction that appends command line args to a serialised file
'''

import json
import sys
serialise = __import__('5-save_to_json_file').save_to_json_file
deserialise = __import__('6-load_from_json_file').load_from_json_file

cmd_text = [item for item in sys.argv[1:]]

try:
    python_text = deserialise('add_item.json')
    print(python_text, type(python_text))
#    for item in cmd_text:
#        python_tex.append(item)
#    serialise(python_text, 'add_item.json')
except Exception:
    serialise(cmd_text, 'add_item.json')
    raise
