#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Output file for all tasks
OUTPUT_FILE = "combined_output.txt"

# Mapper Function for Task 1
def mapper_task1():
    for line in sys.stdin:
        # Split the input line into columns
        columns = line.strip().split(',')
        # Extract relevant data for Task 1
        if len(columns) == 43:  # Ensure all columns are present
            value = columns[10]  # Value column
            if value != '€0':
                country = columns[4]
                height = columns[28]  # Height column
                if height.isdigit():  # Check if height is a valid integer
                    yield "{}\t{}\n".format(country, height)

# Reducer Function for Task 1
def reducer_task1():
    country_height = {}
    count = {}
    for line in sys.stdin:
        country, height = line.strip().split('\t')
        height = int(height)
        if country in country_height:
            country_height[country] += height
            count[country] += 1
        else:
            country_height[country] = height
            count[country] = 1

    for country in country_height:
        avg_height = float(country_height[country]) / count[country]
        yield "{}\t{}\n".format(country, avg_height)

# Mapper Function for Task 2
def mapper_task2():
    for line in sys.stdin:
        # Split the input line into columns
        columns = line.strip().split(',')
        # Extract relevant data for Task 2
        if len(columns) == 43:  # Ensure all columns are present
            value = columns[10]  # Value column
            if value != '€0':
                preferred_foot = columns[14]  # Preferred Foot column
                value = columns[10]  # Value column
                yield "{}\t{}\n".format(preferred_foot, value)

# Reducer Function for Task 2
def reducer_task2():
    foot_value = {}
    count = {}
    for line in sys.stdin:
        preferred_foot, value = line.strip().split('\t')
        value = int(value.strip('€').strip('K'))
        if preferred_foot in foot_value:
            foot_value[preferred_foot] += value
            count[preferred_foot] += 1
        else:
            foot_value[preferred_foot] = value
            count[preferred_foot] = 1

    for foot in foot_value:
        avg_value = float(foot_value[foot]) / count[foot]
        yield "{}\t€{}K\n".format(foot, avg_value)

if __name__ == "__main__":
    # Open the output file in append mode
    with open(OUTPUT_FILE, "a") as output_file:
        # Execute Task 1
        for line in mapper_task1():
            output_file.write(line)
        for line in reducer_task1():
            output_file.write(line)

        # Execute Task 2
        for line in mapper_task2():
            output_file.write(line)
        for line in reducer_task2():
            output_file.write(line)
