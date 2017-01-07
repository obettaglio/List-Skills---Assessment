"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    odd_list = []
    for num in numbers:
        if num % 2 != 0:    #test if num is odd
            odd_list.append(int("{}".format(num)))
    return odd_list

all_odd([1, 2, 7, -5])
all_odd([2, -6, 8])


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo
    
    """
    
    #test passes but unsolved

    i = 0
    for item in items:
        print "{} {}".format(
            i, 
            item
            )
        i = i + 1
        #need new method to count^

print_indices(["Toyota", "Jeep", "Volvo"])
print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']
        
    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    foods1 = set(foods1)            #sets can compare contents
    foods2 = set(foods2)
    common_foods_set = foods1 & foods2
    common_foods_list = list(common_foods_set)
    common_foods_list.sort()        #returns nothing
    return common_foods_list


foods_in_common(["cheese", "bagel", "cake", "kale", "zebra cakes"], ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ])
foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    return [item for item in items if items.index(item) % 2 == 0]

every_other_item([1, 2, 3, 4, 5, 6])
every_other_item(["you", "z", "are", "z", "good", "z", "at", "x", "code"])


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    items.sort()            #sort lowest to highest
    if n > 0:
        items = items[-n:]  #list = last n items
    else:
        items = []
    return items

largest_n_items([2, 6006, 700, 42, 6, 59], 3)
largest_n_items([3, 4, 5], 0)
largest_n_items([3, 3, 3, 2, 1], 2)


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
