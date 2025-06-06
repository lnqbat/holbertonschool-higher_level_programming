#!/usr/bin/env python3
"""
Takes the name of a CSV file.
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts its content to a JSON file.
    """
    try:
        with open(
            csv_filename, mode='r', newline='', encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
