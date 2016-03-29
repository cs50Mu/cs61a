# CS 61A Summer 2014
# Name:
# Login:

from operator import add, sub, mul
from ucb import main


def scheme_exp(n):
    """If n == 1, returns a Scheme program that computes 48/(2*(9+3))
    Otherwise, returns a Scheme program that computes (48/2)*(9+3)

    NOTE: These doctests use eval_string, which will not work until
    you have completed the entire homework.

    >>> first = scheme_exp(1)
    >>> assert '/' in first and '*' in first and '+' in first
    >>> assert '48' in first and '2' in first
    >>> assert '9' in first and '3' in first
    >>> eval_string(first)
    2.0
    >>> second = scheme_exp(2)
    >>> assert '/' in second and '*' in second and '+' in second
    >>> assert '48' in second and '2' in second
    >>> assert '9' in second and '3' in second
    >>> eval_string(second)
    288.0
    """
    if n == 1:
        "*** YOUR CODE HERE ***"
        return '(/ 48 (* 2 (+ 9 3)))'
    else:
        "*** YOUR CODE HERE ***"
        return '(* (/ 48 2) (+ 9 3))'


def tokenize(s):
    """Splits the provided string into a list of tokens.

    >>> tokenize('(* (+ 12 3) 5)')
    ['(', '*', '(', '+', '12', '3', ')', '5', ')']
    """
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    return s.split()



def numberize(atomic_exp):
    """Converts atomic_exp to a number if possible, otherwise leaves
    it alone.  atomic_exp is guaranteed to be a single token, and will
    not be a parenthesis.

    >>> numberize('123')
    123
    >>> numberize('3.14159')
    3.14159
    >>> numberize('+')
    '+'
    """
    # Consider doing int(atomic_exp) and float(atomic_exp).
    # What does int('123') do?  What does int('+') do?
    "*** YOUR CODE HERE ***"
    try:
        result = int(atomic_exp)
    except ValueError:
        try:
            result = float(atomic_exp)
        except ValueError:
            result = atomic_exp
    return result


def read_exp(tokens):
    """Given a list of tokens, returns the first calculator expression
    (either a number, operator, or combination), and the rest of the
    expression that has not been turned into an expression.

    >>> exp, unevaled = read_exp(['(', '+', '2', '3', '6', ')'])
    >>> print_linked_list(exp)
    < '+' 2 3 6 >
    >>> unevaled
    []
    >>> exp, unevaled = read_exp(['2', '3'])
    >>> exp
    2
    >>> unevaled
    ['3']
    >>> exp, unevaled = read_exp(['(', '/', '6', '2', ')', '(', '-', '2', ')'])
    >>> print_linked_list(exp)
    < '/' 6 2 >
    >>> unevaled
    ['(', '-', '2', ')']
    >>> exp, unevaled = read_exp(['(','*','4','(','-','12','8',')',')','3','2'])
    >>> print_linked_list(exp)
    < '*' 4 < '-' 12 8 > >
    >>> unevaled
    ['3', '2']
    """
    if tokens == []:
        raise SyntaxError('unexpected end of input')
    token, rest = tokens[0], tokens[1:]
    if token == ')':
        raise SyntaxError('unexpected )')
    elif token == '(':
        if rest == []:
            raise SyntaxError('mismatched parentheses')
        elif rest[0] == ')':
            raise SyntaxError('empty combination')
        "*** YOUR CODE HERE ***"
        exp, unevaled = read_until_close(rest)
        return exp, unevaled

    else:
        "*** YOUR CODE HERE ***"
        return numberize(token), rest


def read_until_close(tokens):
    """Reads up to and including the first mismatched close
    parenthesis, then forms a combination out all of the values read
    up to that point.

    >>> exp, unevaled = read_until_close(['+', '2', '3', ')', '4', ')'])
    >>> print_linked_list(exp)
    < '+' 2 3 >
    >>> unevaled
    ['4', ')']
    >>> exp, unevaled = read_until_close(['+', '(', '-', '2', ')', '3', ')', ')'])
    >>> print_linked_list(exp)
    < '+' < '-' 2 > 3 >
    >>> unevaled
    [')']
    """
    "*** YOUR CODE HERE ***"
    if tokens[0] == ')':
        return empty, tokens[1:]
    first, remaining = read_exp(tokens)
    rest, remaining = read_until_close(remaining)
    return link(first, rest), remaining



def calc_apply(op, args):
    """Applies an operator to a linked list of arguments.

    >>> calc_apply('+', link(12, link(34, empty)))
    46
    >>> calc_apply('-', link(10, link(2, link(3, link(4, empty)))))
    1
    >>> calc_apply('-', link(3, empty))
    -3
    >>> calc_apply('*', empty)
    1
    """
    if op == '+':
        return do_addition(args)
    elif op == '*':
        return do_multiplication(args)
    elif op == '-':
        return do_subtraction(args)
    elif op == '/':
        return do_division(args)
    else:
        raise NameError('unknown operator {}'.format(op))

def do_addition(args):
    return reduce_linked_list(add, 0, args)

def do_multiplication(args):
    return reduce_linked_list(mul, 1, args)

def do_subtraction(args):
    length = len_linked_list(args)
    if length == 0:
        raise TypeError('not enough arguments')
    elif length == 1:
        return -first(args)
    else:
        return first(args) - reduce_linked_list(add, 0, rest(args))

def do_division(args):
    """Applies the division operation to args.
    args must have a length of at least 1, as in do_subtraction.

    >>> do_division(link(4, empty))
    0.25
    >>> do_division(link(7, link(2, empty)))
    3.5
    >>> do_division(link(60, link(2, link(3, link(5, empty)))))
    2.0
    """
    "*** YOUR CODE HERE ***"
    length = len_linked_list(args)
    if length == 0:
        raise TypeError('not enough arguments')
    elif length == 1:
        return 1/first(args)
    else:
        return first(args)/reduce_linked_list(mul, 1, rest(args))

def calc_eval(exp):
    """Evaluates a calculator expression.

    >>> calc_eval(5)
    5
    >>> calc_eval(link('+', link(12, link(3, empty))))
    15
    >>> subexp1 = link('*', link(3, link(4, empty)))
    >>> subexp2 = link('-', link(12, link(9, empty)))
    >>> exp = link('+', link(subexp1, link(subexp2, empty)))
    >>> print_linked_list(exp)
    < '+' < '*' 3 4 > < '-' 12 9 > >
    >>> calc_eval(exp)
    15
    """
    "*** YOUR CODE HERE ***"
    if is_linked_list(exp):
        return calc_apply(first(exp), map_linked_list(calc_eval, rest(exp))) # 擦，递归无所不能啊。。太神奇了
    return exp

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
        

def map_linked_list(f, lst):
    """Returns a list of the results produced by applying f to each
    element in lst.

    >>> my_list = link(1, link(2, link(3, link(4, empty))))
    >>> print_linked_list(map_linked_list(lambda x: x * x, my_list))
    < 1 4 9 16 >
    >>> pokemon = link('bulbasaur', link('charmander', link('squirtle', empty)))
    >>> print_linked_list(map_linked_list(print, pokemon))
    bulbasaur
    charmander
    squirtle
    < None None None >
    """
    if lst == empty:
        return empty
    else:
        return link(f(first(lst)), map_linked_list(f, rest(lst)))

def len_linked_list(lst):
    """Returns the length of the linked list.

    >>> len_linked_list(empty)
    0
    >>> len_linked_list(link(1, link(2, link(3, empty))))
    3
    >>> len_linked_list(link(1, link(link(2, link(3, empty)), empty)))
    2
    """
    if lst == empty:
        return 0
    else:
        return 1 + len_linked_list(rest(lst))

def reduce_linked_list(f, base, lst):
    """Combines all the elements of lst using the binary function f.
    If the elements of the lst are labelled l0, l1, ... ln, then it
    returns f(l0, f(l1, ... f(ln, base) ... ) )

    >>> reduce_linked_list(add, 4, link(1, link(2, link(3, empty))))
    10
    >>> reduce_linked_list(sub, 4, link(1, link(2, link(3, empty))))
    -2
    >>> reduce_linked_list(lambda x, y: str(x) + y, '', link(1, link(2, empty)))
    '12'
    """
    if lst == empty:
        return base
    else:
        return f(first(lst), reduce_linked_list(f, base, rest(lst)))


def eval_string(line):
    exp, extra = read_exp(tokenize(line))
    if extra:
        raise SyntaxError('Not a single expression')
    return calc_eval(exp)

@main
def repl():
    while True:
        try:
            print(eval_string(input('minicalc> ')))
        except (KeyboardInterrupt, EOFError):
            print('Calculation complete.')
            return
        except (SyntaxError, TypeError, NameError, ValueError) as e:
            print(type(e).__name__ + ':', e)



