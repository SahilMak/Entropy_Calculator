#!/usr/bin/env python3.5
import sys
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import getpass

def open_file():
  # Create Tk object
  root = Tk()
  # Hide blank window
  root.withdraw()
  # Get user name
  user = getpass.getuser()
  # Define default open path
  path = 'C:/Users/%s' % user
  # Define file types
  ftypes = (("Text Documents", "*.txt"), ("All Files", "*.*"))
  # Get file name
  root.fileName = askopenfilename(filetypes=ftypes, initialdir=path)
  return root.fileName

# Get file from user
file = open(open_file())
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
