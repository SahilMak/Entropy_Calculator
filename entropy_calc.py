#!/usr/bin/env python3.5
import sys
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Get file from command line
file = open(sys.argv[1])

# Initialize variables
chars = []
counts = []
total = 0
entropy = 0

# Read file
for line in file:
  for element in line:
    if element not in chars:
      chars.append(element)
      counts.append(0)
    counts[chars.index(element)] += 1
    total += 1

# Calculate probabilities
for x in range(len(chars)):
  probs.append(counts[x] / total)

# Calculate entropy
for x in range(len(chars)):
  entropy += -probs[x] * math.log(probs[x], 2)
print(entropy)
