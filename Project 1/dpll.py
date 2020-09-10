import numpy as np
import sys
import os
import random

def backtrack(clauses, literal):
    modified = []
    for clause in clauses:
        if literal in clause: continue
        if -literal in clause:
            c = [x for x in clause if x != -literal]
            if len(c) == 0: return -1
            modified.append(c)
        else:
            modified.append(clause)
    return modified

def get_counter(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter


def pure_literal(clauses):

    counter = get_counter(clauses)
    literals = []
    pure_literals = [ x for x,y in counter.items() if -x not in counter]

    for literal in pure_literals: 
        clauses = backtrack(clauses, literal)

    literals += pure_literals

    return clauses, literals

def unit_propagation(clauses):
    assignment = []
    unit_clauses = [c for c in clauses if len(c) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        clauses = backtrack(clauses, unit[0])
        assignment += [unit[0]]
        if clauses == -1:
            return -1, []
        if not clauses:
            return clauses, assignment
        unit_clauses = [c for c in clauses if len(c) == 1]
    return clauses, assignment


def variable_selection(clauses):
    counter = get_counter(clauses)

    try:
        choice = random.choice(counter)
    except:
        choice = 1

    print(choice)
    return choice

def dpll(clauses, model):
    clauses, pure_literals = pure_literal(clauses)
    clauses, unit_literals = unit_propagation(clauses)
    literals = pure_literals + unit_literals
    if clauses == - 1:
        return []
    if not clauses:
        return literals

    variable = variable_selection(clauses)
    solution = dpll(backtrack(clauses, variable), literals + [variable])

    if not solution:
        solution = dpll(backtrack(clauses, -variable), literals + [-variable])
    return solution




def main():
    cnf = [[-1, -3, -4], [2, 3, -4], [1, -2, 4], [1, 3, 4], [-1, 2, -3],[-5,2],[10]]
    solution = dpll(cnf,[])

    if solution:
        solution += [x for x in range(1, 5 + 1) if x not in solution and -x not in solution]
        solution.sort(key=lambda x: abs(x))
        print ('s SATISFIABLE')
        print ('v ' + ' '.join([str(x) for x in solution]) + ' 0')
    else:
        print ('s UNSATISFIABLE')

if __name__ == "__main__":
    main()
