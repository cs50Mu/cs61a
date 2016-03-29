################################
# Q2: What Would Python Output?#
################################

def welcome():
    if a == 0:
        return 'hello, welcome to your exam'
    return 'prepare for tricks'

def last_night(n):
    for i in range(n):
        return 'exams'

pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 4]
cut = lambda thing: thing[2:]
slice_of = lambda thing: thing[2:8:2]

def mystery(x):
    if x and (x + 1):
        return 'mystery'
    return mystery

########################
# Q4: Here we go again #
########################

def wheres_waldo(linked_list):
    """
    >>> lst = link("Moe", link("Larry", link("Waldo", link("Curly", empty))))
    >>> wheres_waldo(lst)
    2
    >>> wheres_waldo(link(1, link(2, empty)))
    'Nowhere'
    """
    if "CONDITION":
        return "RESULT"
    elif "CONDITION":
        return "RESULT"
    found_him = wheres_waldo(rest(linked_list))
    if "CONDITION":
        return "RESULT"
    return "RESULT"

###############################
# Q5: Piled Higher and Deeper #
###############################

def inhexing(lst, hex, n):
    """
    >>> inhexing([1, 2, 3, 4, 5], lambda x: 'Poof!', 2)
    [1, 'Poof!', 3, 'Poof!', 5]
    >>> inhexing([2, 3, 4, 5, 6, 7, 8], lambda x: x + 10, 3)
    [2, 3, 14, 5, 6, 17, 8]
    """
    result = "INITIAL"
    for i in range(len(lst)):
        if "CONDITION":
            "ACTION"
        else:
            "ACTION"
    return "RESULT"
def deep_inhexing(lst, hex, n):   # 又是递归  没怎么弄懂。。
    """
    >>> deep_inhexing([1, 2, 3, 4, 5, 6], lambda x: x + 10, 3)
    [1, 2, 13, 4, 5, 16]
    >>> deep_inhexing([1, [[2]], [3, 4, [5]]], lambda x: 'Poof!', 1)
    ['Poof!', [['Poof!']], ['Poof!', 'Poof!', ['Poof!']]]
    >>> deep_inhexing([1, [2], 3], lambda x: 'Poof!', 2)
    [1, [2], 3]
    >>> deep_inhexing([1, [2, 3], 4, [5, 6]], lambda x: 'Poof!', 2)
    [1, [2, 'Poof!'], 4, [5, 'Poof!']]
    >>> deep_inhexing([[2, 3], 4, [5, 6], [7]], lambda x: 'Poof!', 2)
    [[2, 'Poof!'], 'Poof!', [5, 'Poof!'], [7]]
    >>> deep_inhexing([2, [4, [6, [8, 10]]]], lambda x: 'Poof!', 2)
    [2, [4, [6, [8, 'Poof!']]]]
    """    
    def helper(lst, counter):
        if lst == []:
            return []
        first, rest = lst[0], lst[1:]
        if type(first) == type([]):
            return [helper(first,1)] + helper(rest, counter+1)
        elif counter % n == 0:
            return [hex(first)] + helper(rest, counter+1)
        else:
            return [first] + helper(rest, counter+1)
    return helper(lst, 1)
print(deep_inhexing([1, [2, 3], 4, [5, 6]], lambda x: 'Poof!', 2))

##########################
# Q7: Recursion on Trees #
##########################

def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5)  # Sums of partial paths like 2 -> 3 don't count
    False
    """
    if children(t) == []:
        return "RESULT"
    for VARIABLENAME in "SEQUENCE":
        if "CONDITION":
            return "RESULT"
    return False

#######################
# Q9: Newton's Method #
#######################

def phi_approx():
    """
    >>> guess = phi_approx()
    >>> close_to_phi(guess)
    True
    """
    return "FUNCTION"("ARGUMENTS")

########################
# Predefined Functions #
########################


# Functional representation of pairs

# Don't worry if you don't understand this yet.
class PairError(Exception):
    pass

def cons(a, b):
    def answer(m):
        if m == 'car':
            return a
        elif m == 'cdr':
            return b
        else:
            # This is a way for us to create our own error messages.
            raise PairError('You can only use car or cdr on a pair!')
    return answer

def car(p):
    """
    >>> car(cons(1, 2))
    1
    """
    return p('car')

def cdr(p):
    """
    >>> cdr(cons(1, 2))
    2
    """
    return p('cdr')

def is_pair(pair):
    """
    >>> is_pair(cons(1, 2))
    True
    >>> is_pair(1)
    False
    >>> is_pair(lambda x: x)
    False
    >>> is_pair([1, 2])
    False
    """
    try:
        pair('invalid')
        return False
    except PairError:
        return True
    except:
        return False


# Implementation of linked lists using cons

# Don't worry if you don't understand this yet.
class ListError(Exception):
    pass

empty = lambda: 42

def link(element, lst):
    return cons(element, lst)

def first(lst):
    """
    >>> first(link(1, link(2, empty)))
    1
    """
    if lst == empty:
        # This is a way for us to create our own error messages.
        raise ListError('Cannot call first on the empty list!')
    return car(lst)

def rest(lst):
    """
    >>> rest(rest(link(1, link(2, empty)))) == empty
    True
    >>> first(rest(link(1, link(2, empty))))
    2
    """
    if lst == empty:
        # This is a way for us to create our own error messages.
        raise ListError('Cannot call rest on the empty list!')
    return cdr(lst)

def is_linked_list(lst):
    """
    >>> is_linked_list(empty)
    True
    >>> is_linked_list(link(1, link(4, link(7, empty))))
    True
    >>> is_linked_list(link(1, link(4, 7)))
    False
    >>> is_linked_list(link(link(2, empty), empty))
    True
    """
    return lst == empty or (is_pair(lst) and is_linked_list(rest(lst)))

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_linked_list(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))
        
# Tree definition
def tree(node, children=[]):
    return lambda dispatch: node if dispatch == 'node' else children

def datum(tree):
    return tree('node')

def children(tree):
    return tree('children')

t = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def iter_improve(guess, done, update):
    """
    Repeatedly updates guess until it's done.
    """
    while not done(guess):
        guess = update(guess)
    return guess


tolerance = 1e-14

def find_zero(f, df, x=1):
    """
    Takes in a function, its derivative, and an initial
    guess, and approximates the value of x for which
    the function is 0.
    """
    def done(x):
        return abs(f(x)) < tolerance
    def update(x):
        return x - ( f(x) / df(x) )
    return iter_improve(x, done, update)

dx = 1e-6
def deriv(f):
    """
    Takes in a function f and returns its derivative.
    """
    def df(x):
        return (f(x + dx) - f(x)) / dx
    return df

def easy_find_zero(f, x=1):
    """
    Takes in a function and an initial guess, and approximates
    the value of x for which the function is 0.
    """
    return find_zero(f, deriv(f), x)


from math import sqrt

phi = (1 + sqrt(5))/2
error = 1e-10

def close_to_phi(x):
	return abs(phi - x) <= error 

