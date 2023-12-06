"""
Template for Programming Assignment FIT1045 - OCT 2021
Family Trees

In this assignment we create a Python module to implement some
basic family tree software, where users can look up various relationships
that exist in the database, as well as merging two family tree databases
that may contain overlapping information.

Functions  1-7 are due in Part 1 of the assignment. Functions
for 8 and 9 are due in Part 2.

We represent each entry in a family tree database as a list of three
strings [name, father, mother], where name is a person's name, father
is the name of their father, and mother is the name of their mother.
Where a particular relationship is unknown, the value None is used.
For example:

>>> duck_tree = [['Fergus McDuck', None, None],
...           ['Downy ODrake', None, None],
...           ['Quackmore Duck', None, None],
...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Huey Duck', None, 'Della Duck'],
...           ['Dewey Duck', None, 'Della Duck'],
...           ['Louie Duck', None, 'Della Duck']]


The file hobbit-family.txt is also provided for testing. The database
used in this file has been compiled using the info at
http://lotrproject.com/hobbits.php. Character names are by J.R.R. Tolkein.

For more information see the function documentations below and the
assignment sheet.

"""


# Part 1 (due Week 6) #

def read_family(filename):
    """
    Input: A filename (filename) containing a family tree database where
    each line is in the form name, father, mother
    Output: A family tree database containing the contents of the file
    in the format specified above, or None if the file is in the incorrect
    format.
    
    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> len(hobbits)
    119
    >>> hobbits[118]
    ['Sancho Proudfoot', 'Olo Proudfoot', None]

     """
    with open(filename) as file:
        lst=[]
        for row in file:
            row = row.strip()
            row = row.split(',')
            lst.append(row)
            for name in range(len(row)):
                row[name] = row[name].strip()
                if row[name] == '':
                    row[name] = None
    return lst    





def person_index(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The index value of the person's entry in the family tree,
            or None if they have no entry.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> person_index('Dewey Duck', duck_tree)
    8
    >>> person_index('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        for j in range(len(family[i])):
            if family[i][0] == person:
                return i


                
def father(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's father, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> father('Della Duck', duck_tree)
    'Quackmore Duck'
    >>> father('Huey Duck', duck_tree)

    >>> father('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        dad = family[i][1]
        if family[i][0] == person:
            return dad
        

def mother(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's mother, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> mother('Hortense McDuck', duck_tree)
    'Downy ODrake'
    >>> mother('Fergus McDuck', duck_tree)

    >>> mother('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        mum = family[i][2]
        if family[i][0] == person:
            return mum


def children(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all of person's children.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(children('Della Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> children('Donald Duck', duck_tree)
    []
    >>> sorted(children('Fergus McDuck', duck_tree))
    ['Hortense McDuck', 'Scrooge McDuck']
    >>> children('Donald Mallard', duck_tree)
    []
    
    """
    children = []
    for i in range(len(family)):
        for j in range(1, len(family[i])):
                if family[i][j] == person:
                    children.append(family[i][0])
    return children

def grandchildren(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing only the names of the grandchildren of person
        that are stored in the database.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(grandchildren('Quackmore Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> sorted(grandchildren('Downy ODrake', duck_tree))
    ['Della Duck', 'Donald Duck']
    >>> grandchildren('Della Duck', duck_tree)
    []
    
    """
    grandchild = []   
    for i in range(len(family)):
        for j in range(1, len(family[i])):
                if family[i][j] == person:
                    '''find children of person'''
                    child = family[i][0]
                    '''find grandchildren of person'''
                    grandson_granddaughter = children(child, family)
                    for n in range(len(grandson_granddaughter)):
                        grandchild.append(grandson_granddaughter[n])
    return grandchild


def cousins(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all cousins of person that
            are stored in the database.
    
    For example:
    
    >>> hobbits = read_family('hobbit-family.txt')
    >>> sorted(cousins('Frodo Baggins', hobbits))
    ['Daisy Baggins', 'Merimac Brandybuck', 'Milo Burrows', 'Saradoc Brandybuck', 'Seredic Brandybuck']
    
    """
    parents = []
    cousins = []
    for i in range(len(family)):
        for j in range(len(family[i])):
            if family[i][j] == person:
                '''find parents of person'''
                parents.append(father(family[i][j], family))
                parents.append(mother(family[i][j], family))
                for k in range(len(parents)):
                    '''find grandfather of person'''
                    grandfather = father(parents[k], family)
                    grandchild = grandchildren(grandfather, family)
                    for x in range(len(grandchild)):
                        '''if same father, grandchild[x] = siblings'''
                        if father(grandchild[x], family) not in parents:
                            '''excluding out sibilings'''
                            if grandchild[x] not in cousins:
                                cousins.append(grandchild[x])
                        '''if same mother, grandchild[x] = siblings'''
                        if mother(grandchild[x], family) not in parents:
                            '''to prevent it append to same name in the list,
                                check if it is in the list, then dont append into the list again
                                '''
                            if grandchild[x] not in cousins:
                                cousins.append(grandchild[x])
    return cousins    


# Part 2: (due Week 11) #
# to find parents of person
def parents(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's parents, or empty list if the information is
            not in the database.
    """
    parents = []
    # reusing function father and mother from Assignment Part 1
    dad = father(person, family)
    mum = mother(person, family)
    if dad != None:
        parents.append(dad)
    if mum != None:
        parents.append(mum)
    return parents

# to find how many generations apart in a list(lst)
def ancestors_generations(lst, family):
    """
    Input : A list of ancestors(lst) and a family tree database (family)
            as specified above.
    Output: The number of generations apart.
    """
    i = 1
    generation = 0
    while i < len(lst):
        # reusing function parents
        if lst[-i] in parents(lst[-i-1], family):
            generation += 1
            i += 1
        else:
            lst.pop(-i-1)
    return generation

# to find the ancestors of person
def find_ancestors(person, family):
    """
    Input : A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's ancestors, or empty list if the information is
            not in the database.
    """
    ancestors = []
    boundary_parents = [person]
    while len(boundary_parents) > 0:
        b = boundary_parents.pop()
        ancestors += [b]
        # reusing function parents to get the list of parents of person
        for j in parents(b, family):
            if j not in ancestors and j not in boundary_parents:
                boundary_parents.append(j)      
    return ancestors


def direct_ancestor(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: One of the following three string outputs (where p1 and
            p2 are the given input strings, and n is a non-negative integer):
            "p1 is a direct ancestor of p2, n generations apart."
            "p2 is a direct ancestor of p1, n generations apart."
            "p1 is not a direct ancestor or descendant of p2."

    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> direct_ancestor('Frodo Baggins', 'Frodo Baggins', hobbits)
    'Frodo Baggins is a direct ancestor of Frodo Baggins, 0 generations apart.'
    >>> direct_ancestor('Frodo Baggins', 'Gormadoc Brandybuck', hobbits)
    'Gormadoc Brandybuck is a direct ancestor of Frodo Baggins, 5 generations apart.'
    
    """
    ancestors = []
    descendants = []
    generation = 0
    boundary_parents = [p1]
    boundary_children = [p1]
    txt = "{ancestor} is a direct ancestor of {descendant}, {generation} generations apart."
    # if p1 == p2, then they are the same person with 0 generation apart
    if p1 == p2:
        return (txt.format(ancestor = p1, descendant = p2, generation = 0))
    # if p1 != p2, enter while loop to find is p2 an ancestor of p1
    while len(boundary_parents) > 0:
        b = boundary_parents.pop()
        ancestors += [b]
        # goals = p2, if b == p2, ancestor is found
        if b == p2:
            # using function ancestors_generations to find how many generation apart between p1 and p2
            generation = ancestors_generations(ancestors, family)
            return (txt.format(ancestor = p2, descendant = p1, generation = generation))
        # if b != p2, goals haven't been reached yet, append parents of b into boundary list
        else:
            # resuing function parents
            for j in parents(b, family):
                # if not in ancestors means it haven't been check yet
                # if not in boundary_parents means it is not in the list of waiting to check
                if j not in ancestors and j not in boundary_parents:
                    # append into boundary list waiting to be checked
                    boundary_parents.append(j) 
    # if p2 is not an ancestor of p1, find is p2 a descendant of p1
    while len(boundary_children) > 0:
        b = boundary_children.pop()
        descendants += [b]
        # goals = p2, if b == p2, descendents is found
        if b == p2:
            # find how many generation apart between p1 and p2
            i = 1
            while i < len(descendants):
                if descendants[-1] in children(descendants[-i-1], family):
                    generation += 1
                    i += 1
                else:
                    descendants.pop(-i-1)
            return (txt.format(ancestor = p1, descendant = p2, generation = generation))
        # if b != p2, goals haven't been reached yet, append children of b into boundary list
        else:
            # resuing function children
            for j in children(b, family):
                # if not in descendants means it haven't been check yet
                # if not in boundary_children means it is not in the list of waiting to check
                if j not in descendants and j not in boundary_children:
                    # append into boundary list waiting to be checked
                    boundary_children.append(j)          
    return (p1 + " is not a direct ancestor or descendant of " + p2 + ".")


def cousin_degree(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: A number representing the minimum distance cousin relationship between p1 and p2, as follows:
            -   0 if p1 and p2 are siblings
            -   1 if p1 and p2 are cousins
            -   n if p1 and p2 are nth cousins, as defined at https://www.familysearch.org/blog/en/cousin-chart/
            -   -1 if p1 and p2 have no cousin or sibling relationship
    
    For example:
    >>> hobbits = read_family("hobbit-family.txt")
    >>> cousin_degree('Minto Burrows', 'Myrtle Burrows', hobbits)
    0
    >>> cousin_degree('Estella Bolger', 'Meriadoc Brandybuck', hobbits)
    3
    >>> cousin_degree('Frodo Baggins', 'Bilbo Baggins', hobbits)
    -1
    
    """
    # reusing function find_ancestors to find ancestors of p1 and p2
    p1_ancestor = find_ancestors(p1, family)
    p2_ancestor = find_ancestors(p2, family)
    for i in p1_ancestor:
        if i in p2_ancestor:
            # slice the ancestors from p1 & p2 to their common ancestor
            ancestor1 = p1_ancestor[:p1_ancestor.index(i) + 1]
            ancestor2 = p2_ancestor[:p2_ancestor.index(i) + 1]
            # if they are at the same generation then they are cousin
            if ancestors_generations(ancestor1, family) == ancestors_generations(ancestor2, family):
                generation = ancestors_generations(ancestor1, family)
                # cousin_degree = generation - 1
                degree = generation - 1
                return degree
    # no cousin or sibling relationship
    return -1
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
