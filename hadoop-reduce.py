#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Mapper Function for Task 1
def mapper_task1(output_file):
    results = []
    for line in sys.stdin:
        # Split the line into columns
        columns = line.strip().split(',')
        if len(columns) == 43:  # Ensure all columns are present
            value = columns[10]  # Value column
            if value != '€0':
                country = columns[4]
                height = columns[28]  # Height column
                if height.isdigit():  # Check if height is a valid integer
                    results.append("{}\t{}".format(country, height))

    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

# Reducer Function for Task 1
def reducer_task1(input_file, output_file):
    country_height = {}
    count = {}
    with open(input_file, 'r') as file:
        for line in file:
            country, height = line.strip().split('\t')
            height = int(height)
            if country in country_height:
                country_height[country] += height
                count[country] += 1
            else:
                country_height[country] = height
                count[country] = 1

    with open(output_file, 'w') as file:
        for country in country_height:
            avg_height = float(country_height[country]) / count[country]
            file.write("{}\t{}\n".format(country, avg_height))

# Mapper Function for Task 2
def mapper_task2(output_file):
    results = []
    for line in sys.stdin:
        # Split the line into columns
        columns = line.strip().split(',')
        if len(columns) == 43:  # Ensure all columns are present
            value = columns[10]  # Value column
            if value != '€0':
                preferred_foot = columns[14]  # Preferred Foot column
                value = columns[10]  # Value column
                results.append("{}\t{}".format(preferred_foot, value))

    with open(output_file, 'w') as file:
        file.write('\n'.join(results))

# Reducer Function for Task 2
def reducer_task2(input_file, output_file):
    foot_value = {}
    count = {}
    with open(input_file, 'r') as file:
        for line in file:
            preferred_foot, value = line.strip().split('\t')
            value = int(value.strip('€').strip('K'))
            if preferred_foot in foot_value:
                foot_value[preferred_foot] += value
                count[preferred_foot] += 1
            else:
                foot_value[preferred_foot] = value
                count[preferred_foot] = 1

    with open(output_file, 'w') as file:
        for foot in foot_value:
            avg_value = float(foot_value[foot]) / count[foot]
            file.write("{}\t€{}K\n".format(foot, avg_value))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combined_script.py <task> <output_file>")
        sys.exit(1)

    task = sys.argv[1]
    output_file = sys.argv[2]

    if task == "mapper_task1":
        mapper_task1(output_file)
    elif task == "reducer_task1":
        reducer_task1(sys.stdin, output_file)
    elif task == "mapper_task2":
        mapper_task2(output_file)
    elif task == "reducer_task2":
        reducer_task2(sys.stdin, output_file)
    else:
        print("Invalid task name")
        sys.exit(1)