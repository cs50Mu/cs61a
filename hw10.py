# CS 61A Summer 2014
# Name:
# Login:

class Tree:
    def __init__(self, datum, *args):
        self.datum = datum
        self.children = []
        for tree in args:
            self.children.append(tree)
    def pretty_print(self, indent=''):
        """ Prints the tree.
        >>> t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6)))
        >>> t.pretty_print()
        1
        |__2
        |  |__4
        |  |__5
        |__3
           |__6
           
        >>> Tree(0, Tree('hello'), Tree('world'), Tree('!')).pretty_print()
        0
        |__hello
        |__world
        |__!
        >>> Tree(0, Tree('hello', Tree('world')), Tree('Goodbye')).pretty_print()
        0
        |__hello
        |  |__world
        |__Goodbye

        """
        if not indent:
            print(self.datum)
        else:
            print(indent[:-3] + '|__' + str(self.datum))

        if self.children:
            for child in self.children[:-1]:
                child.pretty_print(indent + '|  ')
            self.children[-1].pretty_print(indent + '   ')


class HuffmanTree(Tree):
    def __init__(self, *children):
        letters = []
        for child in children:
            letters += child.datum
        Tree.__init__(self, letters, *children)

        # Actually creating the encoding
        while len(self.children) > 2:
            self.merge_two_smallest()

    def merge_two_smallest(self):
        smallest = min(self.children, key=lambda x: x.frequency)
        "*** YOUR CODE HERE ***"        
        self.children.remove(smallest)
        smaller = min(self.children, key=lambda x: x.frequency)
        self.children.remove(smaller)
        self.children.append(HuffmanTree(smallest, smaller))

    @property
    def left_child(self):
        assert len(self.children) == 2
        return self.children[0]

    @property
    def right_child(self):
        assert len(self.children) == 2
        return self.children[1]

    @property
    def frequency(self):
        return sum([child.frequency for child in self.children])

    def encode_character(self, character):
        """ Returns a string representing the Huffman encoding of the
        character.

        >>> t = make_example_huffman_tree()
        >>> t.encode_character('E')
        '1100'
        >>> [t.encode_character(letter) for letter in t.datum]
        ['0', '100', '1010', '1011', '1100', '1101', '1110', '1111']
        """
        assert character in self.datum
        "*** YOUR CODE HERE ***"
#        result = ''
#        while len(self.children) >= 1:
#            if character in self.left_child.datum:
#                result += '0'
#                self = self.left_child
#
#            elif character in self.right_child.datum:
#                result += '1'
#                self = self.right_child
#        return result
        if character in self.left_child.datum:   # A more elegant recursive solution
            return '0' + self.left_child.encode_character(character)
        else:
            return '1' + self.right_child.encode_character(character)

    def encode(self, string):
        """ Returns a string representing the Huffman encoding of the
        character.

        >>> t = make_example_huffman_tree()
        >>> t.encode('BACADAEAFABBAAAGAH')
        '100010100101101100011010100100000111001111'
        """
        result = ''
        for character in string:
            result += self.encode_character(character)
        return result

    def decode_character(self, code):
        """ Decodes a single character from code.
        Returns the character, and the rest of the code (that has not
        been decoded yet).
        code is a Huffman encoding created from this HuffmanTree.

        >>> t = make_example_huffman_tree()
        >>> t.decode_character('0')
        ('A', '')
        >>> t.decode_character('10001010')
        ('B', '01010')
        """
        "*** YOUR CODE HERE ***"
        first, rest  = code[0], code[1:]
        if first == '0':
            return self.left_child.decode_character(rest)
        elif first == '1':
            return self.right_child.decode_character(rest)



    def decode(self, code):
        """ Decodes code to recover the original message.
        code is a Huffman encoding created from this HuffmanTree.

        >>> t = make_example_huffman_tree()
        >>> t.decode('100010100101101100011010100100000111001111')
        'BACADAEAFABBAAAGAH'
        """
        result = ''
        while code:
            character, code = self.decode_character(code)
            result += character
        return result

    # Utility method for making the Huffman tree canonical
    def sort_by_frequency(self):
        self.datum.sort()
        self.children.sort(key=lambda x: x.frequency, reverse=True)
        for child in self.children:
            child.sort_by_frequency()

class HuffmanLeaf(Tree):
    def __init__(self, letter, frequency):
        Tree.__init__(self, [ letter ])
        self.letter = letter
        self.frequency = frequency

    def encode_character(self, character):
        assert character == self.letter
        "*** YOUR CODE HERE ***"
        return ''  # 递归终止条件 HuffmanLeaf类有单独的encode_character method

    def decode_character(self, code):
        """ Decodes a character.  Since a leaf has only one letter, it
        must be that letter.

        >>> leaf = HuffmanLeaf('A', 50)
        >>> leaf.decode_character('010')
        ('A', '010')
        """
        "*** YOUR CODE HERE ***"
        return self.letter, code  # HuffmanLeaf类有单独的decode_character method

    # Utility method for making the Huffman tree canonical
    def sort_by_frequency(self):
        pass

def make_huffman_tree(letters, frequencies):
    """ Generates a Huffman tree that gives the optimal
    variable-length prefix encoding for letters given the
    frequencies.

    >>> huff_tree = make_example_huffman_tree()
    >>> huff_tree.pretty_print()
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    |__['A']
    |__['B', 'C', 'D', 'E', 'F', 'G', 'H']
       |__['B', 'C', 'D']
       |  |__['B']
       |  |__['C', 'D']
       |     |__['C']
       |     |__['D']
       |__['E', 'F', 'G', 'H']
          |__['E', 'F']
          |  |__['E']
          |  |__['F']
          |__['G', 'H']
             |__['G']
             |__['H']
    """
    assert len(letters) == len(frequencies)
    children = []
    for i in range(len(letters)):
        children.append(HuffmanLeaf(letters[i], frequencies[i]))
    return HuffmanTree(*children)


# Utility function for use in doctests
def make_example_huffman_tree():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    frequencies = [1000, 300, 105, 104, 103, 102, 101, 100]
    tree = make_huffman_tree(letters, frequencies)
    tree.sort_by_frequency()
    return tree


############
# Optional #
############

def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.

    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    "*** YOUR CODE HERE ***"
#    count = 0
#    def count_wrapper(*args):
#        nonlocal count
#        count +=1
#        return f(*args)
#    
#    def call_report():
#        nonlocal count
#        return count
#
#    return count_wrapper, call_report
    calls = 0
    def counted(*args):
        nonlocal calls
        calls += 1        # a more elegant solution 直接省掉了一个函数声明
        return f(*args)
    return counted, lambda: calls



class foo:
    """
    >>> foo.y
    []
    >>> foo.x
    3
    >>> cat = foo('Meow')
    >>> cat.speak()
    Meow
    >>> cat.x
    4
    >>> foo = foo(foo) # OMG WHY
    >>> foo.x
    5
    >>> bar = foo.bar('hello!')
    >>> bar.speak()
    hello!
    >>> cat.x
    4
    """
    "*** YOUR CODE HERE ***"
    x = 3
    y = []
    def __init__(self, word):
        self.bar = word
        foo.x += 1
        self.x = foo.x

    def speak(self):
        print(self.bar)

class new_foo:
    "Add your solution to the previous part, replacing foo with new_foo and bar with new_bar.  DO NOT ADD ANY DOCTESTS TO THIS CLASS."
    x = 3
    y = []
    def __init__(self, word):
        self.new_bar = word
        new_foo.x += 1
        self.x = new_foo.x

    def speak(self):
        print(self.new_bar)


class baz(new_foo):
    """ Note:  First we redo the doctests from the previous question.
    >>> new_foo.y
    []
    >>> new_foo.x
    3
    >>> cat = new_foo('Meow')
    >>> cat.speak()
    Meow
    >>> cat.x
    4
    >>> new_foo = new_foo(new_foo) # OMG WHY
    >>> new_foo.x
    5
    >>> new_bar = new_foo.new_bar('hello!')
    >>> new_bar.speak()
    hello!
    >>> cat.x
    4
    >>> baz.y
    []
    >>> cat.y.append(2)
    >>> new_foo.new_bar.y
    [2]
    >>> baz.y
    [2]
    >>> new_foo.new_bar.x
    6
    >>> baz = baz(baz, baz) # ARGHHHH
    >>> new_foo.new_bar.x
    7
    >>> baz.add_to_parent_y(4)
    >>> baz.y
    [2, 4]
    >>> baz.new_bar.y
    [2, 4]
    >>> new_foo.new_bar.y
    [2, 4]
    >>> baz.add_to_baz_y(6)
    >>> baz.y
    [2, 4, 6]
    >>> baz.new_bar.y
    [2, 4, 6]
    >>> new_foo.new_bar.y
    [2, 4]
    >>> baz.add_to_parent_y(8)
    >>> baz.y
    [2, 4, 6]
    >>> baz.new_bar.y
    [2, 4, 6]
    >>> new_foo.new_bar.y
    [2, 4, 8]
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, x, y):
        new_foo.__init__(self,x)
        self.garply = y

    def add_to_parent_y(self, num):
        new_foo.y.append(num)
    
    def add_to_baz_y(self, num):
        baz.y = baz.y + [ num ]

import doctest
doctest.testmod()
