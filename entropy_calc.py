#!/usr/bin/env python3.5
import sys
import math

# Get file from command line
file = open(sys.argv[1])

# Initialize variables
chars = []
counts = []
total = []

# Read file
for line in file:
  for element in line:
    if element not in chars:
      chars.append(element)
      counts.append(0)
    counts[chars.index(element)] += 1
    total += 1
