# CS 61A Summer 2014
# Name:
# Login:

########################
# Iterable Linked List #
########################


class Link:
    """A recursive list, with Python integration."""
    empty = None

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ', ' + repr(self.rest)
        return 'Link({}{})'.format(self.first, rest)

    def __str__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ' ' + str(self.rest)[2:-2]
        return '< {}{} >'.format(self.first, rest)

    """
    Implement the iterable interface for the Link class.
    You will need to return an instance of an iterator 
    object in the __iter__ method.
    """
    def __iter__(self):
        """
        >>> l = list_to_link([1, 2, 3, 4])
        >>> i = iter(l)
        >>> hasattr(i, '__next__')
        True
        >>> l2 = list_to_link([3, 1, 4, 1])
        >>> for el in l2:
        ...    print(el)
        ...
        3
        1
        4
        1
        """
        "*** YOUR CODE HERE ***"
        return LinkedListIterator(self)



class LinkedListIterator:
    "*** YOUR CODE HERE ***"
    def __init__(self, linked_lst):
        self.lst = linked_lst

    def __next__(self):
        if self.lst == Link.empty:
            raise StopIteration
        val = self.lst.first
        self.lst = self.lst.rest
        return val


def list_to_link(lst):
    """
    This is a convenience method which 
    converts a Python list into a linked list.
    DO NOT USE THIS IN ANY OF YOUR SOLUTIONS.
    """
    ll = Link.empty
    for elem in lst[::-1]:
        ll = Link(elem, ll)
    return ll


################
# Permutations #
################


def list_perms(lst):
    """
    Returns a list of all permutations of lst.
    >>> p = list_perms([1, 2, 3])
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> p1 = list_perms([0, 1])
    >>> p1.sort()
    >>> p1
    [[0, 1], [1, 0]]
    """
    if lst == []:
        return [[]]# REPLACE ME
    prev_perms = list_perms(lst[1:])
    result = []
    for perm in prev_perms:
        for i in range(len(lst)):
            "*** YOUR CODE HERE ***"
            result.append(perm[:i] + [lst[0]] + perm[i:])
    return result

import random

def random_permutation(seq):
    """
    Generates and returns a random permutation
    of the given sequence.
    DO NOT USE THIS IN ANY OF YOUR SOLUTIONS.
    """
    permutation = []
    poss_indices = list(range(len(seq)))
    for _ in range(len(seq)):
        index = random.choice(poss_indices)
        poss_indices.remove(index)
        permutation.append(seq[index])
    return permutation

def interleave(seq, other):
    """
    Returns a new list whose elements 
    alternate between the elements of seq and other.
    DO NOT USE THIS IN ANY OF YOUR SOLUTIONS.
    """
    result = list(seq)
    for i, el in enumerate(other):
        result.insert(2 * i + 1, el)
    return result

class MathPuzzle:
    """
    Randomly generates a math puzzle given a rng.
    Solutions to the math puzzle are represented as 
    a list of numbers from 1 to rng arranged
    in a particular order.
    """
    ops = ['+', '*', '-', '//']

    def __init__(self, rng):
        self.range = rng
        self.puzzle = [random.choice(MathPuzzle.ops) for _ in range(self.range - 1)] # a random list of operators ('+', '-', '*', and '//')
        self.expression = [str(el) for el in interleave(random_permutation(range(1, rng + 1)), self.puzzle)] # operators interwoven with numbers
        self.value = eval(''.join(self.expression)) # the result of evaluating self.expression in Python

    def __str__(self):
        """
        String representation with blanks for numbers.
        """
        return ' '.join([el if el in MathPuzzle.ops else "___" for el in self.expression]) + " = " + str(self.value)

    def check_solution(self, inputs):
        """
        Checks if the given inputs solve the puzzle.
        """
        guessed_exp = [str(el) for el in interleave(inputs, self.puzzle)]
        return eval(''.join(guessed_exp)) == self.value


def solve_list_perms(puzzle):
    """
    Solves a MathPuzzle using a list of permutations;
    returns the first correct answer it encounters.
    """
    "*** YOUR CODE HERE ***"
    l = range(1,puzzle.range + 1)
    for perm in list_perms(l):
        if puzzle.check_solution(perm):
            return perm
    return None



def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    "*** YOUR CODE HERE ***"
    if lst == []:
        yield []
    else:
        for perm in generate_perms(lst[1:]):
            for i in range(lst):
                yield perm[:i] + [lst[0]] + perm[i:]

def solve_gen_perms(puzzle):
    """
    Solves a MathPuzzle by generating permutations;
    returns the first correct answer it encounters.
    """
    "*** YOUR CODE HERE ***"
    l = range(1,puzzle.range + 1)
    for perm in list_perms(l):
        if puzzle.check_solution(perm):
            return perm
    return None


class TestPuzzle(MathPuzzle):
    """
    Creates a MathPuzzle out of the given expression.
    >>> test = TestPuzzle([1, '+', 2, '*', 3])
    >>> print(test)
    ___ + ___ * ___ = 7
    >>> test.check_solution([1, 2, 3])
    True
    >>> test.check_solution([1, 3, 2])
    True
    >>> test.check_solution([2, 3, 1])
    False
    """
    def __init__(self, expression):
        self.expression = [str(el) for el in expression]
        self.puzzle = [el for el in expression if el in MathPuzzle.ops]
        self.value = eval(''.join(self.expression))
        self.range = len(self.puzzle) + 1



##############
# Remainders #
##############

def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m. 

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for i in range(3):
    ...         next(rem_group)
    ...
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def remainder_generator(s):
        delta = 0
        while True:
            yield  delta * m + s
            delta += 1
    for i in range(m):
        yield remainder_generator(i)

import doctest
doctest.testmod
