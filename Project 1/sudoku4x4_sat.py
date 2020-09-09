import numpy as np
import sys
import os

# KNOWLEDGE BASE 
# Importing Sudoku rules from file 
loc = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
filepath = '/test sudokus/sudoku-rules-4x4.txt'
path = loc+filepath

f = open(path, 'r')
lines = f.readlines()
in_data = []
for line in lines:
    in_data.append(line.strip().split('0')[0])
f.close()

# Insert all the clauses in the knowledge base
KB = [[int(n) for n in line.split()] for line in in_data if line[0] not in ('c', 'p')]
print('Total number of clauses in KB:', len(KB))
print('first clause:', KB[0])


# PREMISES 
# Import Sudokus 
filepath = '/test sudokus/4x4.txt'
path = loc+filepath
f = open(path, 'r')
lines = f.readlines()
sudoku4x4 = []
for line in lines:
  sudoku4x4.append(line.strip().split('n')[0])
f.close()
print(sudoku4x4[:5])

# Converting 1st puzzle to CNF

col = 1
row = 1
premises = []
for i in range(len(sudoku4x4[0])):
  if col == 5: 
    col = 1
    row += 1  
  result = ''
  if sudoku4x4[0][i] != '.':
    value = sudoku4x4[0][i]
    result = result + str(row)+str(col)+str(value)
    premises.append([int(result)])
  col += 1
print(premises)

# Preparing Final CNF by combining KB and Premises 
CNF = KB + premises
print(CNF)

#todo: #1 build DPLL SAT solver 
