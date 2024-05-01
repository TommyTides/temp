#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys

# Task 1: Calculate average height per country
def height_mapper(data):
    for row in data:
        country = row['Nationality']
        height = row['Height']
        if height and country:
            print(country + '\t' + height + ',1')

def height_reducer(data):
    current_country = None
    total_height = 0
    total_players = 0

    for row in data:
        country = row[0]
        height, count = row[1].split(',')
        count = int(count)

        if current_country == country:
            total_height += float(height)
            total_players += count
        else:
            if current_country:
                average_height = total_height / total_players
                print(current_country + '\t' + str(average_height))
            current_country = country
            total_height = float(height)
            total_players = count

    if current_country:
        average_height = total_height / total_players
        print(current_country + '\t' + str(average_height))

# Task 2: Remove players with value €0
def value_mapper(data):
    for row in data:
        player_id = row['ID']
        value = row['Value']
        if value != '€0':
            print(player_id + '\t' + ','.join(row.values()))

# Task 3: Calculate average value per preferred foot
def foot_mapper(data):
    for row in data:
        preferred_foot = row['Preferred Foot']
        value = row['Value']
        if preferred_foot and value:
            print(preferred_foot + '\t' + value + ',1')

def foot_reducer(data):
    current_foot = None
    total_value = 0
    total_players = 0

    for row in data:
        foot = row[0]
        value, count = row[1].split(',')
        count = int(count)

        if current_foot == foot:
            total_value += float(value[1:])  # Remove '€' from value
            total_players += count
        else:
            if current_foot:
                average_value = total_value / total_players
                print(current_foot + '\t' + '€{:.2f}K'.format(average_value))
            current_foot = foot
            total_value = float(value[1:])  # Remove '€' from value
            total_players = count

    if current_foot:
        average_value = total_value / total_players
        print(current_foot + '\t' + '€{:.2f}K'.format(average_value))

if __name__ == "__main__":
    script_name = sys.argv[0]

    # Read data from CSV file
    with open('Soccer2019.csv', 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    if 'height' in script_name:
        height_mapper(data)
    elif 'value' in script_name:
        value_mapper(data)
    elif 'foot' in script_name:
        foot_mapper(data)
    elif 'height_avg' in script_name:
        height_reducer(data)
    elif 'foot_avg' in script_name:
        foot_reducer(data)
