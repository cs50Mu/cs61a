def knapsack(weights, values, capacity):
    """Solves knapsack.

    >>> w = link(3, link(2, link(2, empty)))
    >>> v = link(4, link(3, link(3, empty)))
    >>> knapsack(w, v, 4)
    6
    >>> knapsack(w, v, 3)
    4
    >>> knapsack(w, v, 6)
    7
    >>> knapsack(w, v, 100)
    10
    >>> w = link(38, link(63, link(85, link(89, link(82, empty)))))
    >>> w = link(23, link(31, link(29, link(44, link(53, w)))))
    >>> v = link(43, link(67, link(84, link(87, link(72, empty)))))
    >>> v = link(92, link(57, link(49, link(68, link(60, v)))))
    >>> print_linked_list(w)
    <23 31 29 44 53 38 63 85 89 82>
    >>> print_linked_list(v)
    <92 57 49 68 60 43 67 84 87 72>
    >>> knapsack(w, v, 165)
    309
    """
    # Base Case
    if weights == empty:
        return 0

    # Two recursive calls (Making the Problem Smaller)
    without_first = knapsack(rest(weights), rest(values), capacity)
    take_first = knapsack(rest(weights), rest(values), capacity - first(weights))

    # Finding the Solution
    if first(weights) > capacity:
        # Not allowed to take the first item, so only option is without_first
        return without_first
    else:
        # Choose whichever option gives us more profit.
        return max(first(values) + take_first, without_first)


# Implementation of linked lists using cons
empty = lambda: 42

def link(elem, lst):
  return cons(elem, lst)

def first(lst):
  return car(lst)

def rest(lst):
  return cdr(lst)

# You don't have to worry about how
# printed_linked_list works yet.
def print_linked_list(lst):
    print(linked_list_to_str(lst))

def linked_list_to_str(lst):
    if lst == empty:
        return '<>'
    s = '<'
    while lst != empty:
        s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s[:-1] + '>'

# Functional representation of pairs
# You should strive to understand this.
def cons(a, b):
  return lambda m: m(a, b)

def car(p):
  return p(lambda x, y: x)

def cdr(p):
  return p(lambda x, y: y)

# for easy interactive testing
w = link(3, link(2, link(2, empty)))
v = link(4, link(3, link(3, empty)))


