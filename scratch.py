# shit
def tcbin(n):
    """ Binomials """
    l = []
    for i in range(n + 1):
        b = binomial(n, i)
        l.append(b)
        print b
    return l

def pr(n):
    l = []
    for i in range(1,n):
        a,b = 10^(i-1), 10^i
        t = (a, b, b-a, len(prime_range(a,b)))
        l.append(t)
    return l



def nzfactorial(n):
    """
    Calculate factorial of n with trailing zeros stripped.
    http://www.purplemath.com/modules/factzero.htm
    """
    toppow5 = floor(log_b(n,5))
    fivefactors = [n//5^(i+1) for i in range(toppow5)]
    num_zeros = sum(fivefactors)
    nzfact = factorial(n)/10^num_zeros
    print "List of five factors = ", fivefactors
    print "Top power = ", toppow5
    print "Number of zeros = ", num_zeros
    return nzfact
    

def lotto(n):
    import random
    tlist = []
    for j in range(n):
        nums = range(1,47)
        t = []
        for i in range(6):
            if len(nums) > 1:
                t.append(nums.pop(random.randrange(0,len(nums))))
            else:
                t.append(nums[0])
        tlist.append((sorted(t), sum(t)))
    return tlist

def sumdig(n):
    st = str(n)
    # s = sum([int(st[i]) for i in len(st)])
    s = 0
    for i in range(len(st)):
        s += int(st[i])
    if s > 9:
        s = sumdig(s)
    return s




    
def testtot():
    """ Euler totient"""
    l = primes_first_n(50)
    bprod = [i * j for i in l for j in l]
    lprod = [(i - 1) * (j - 1) for i in l for j in l]
    return l, bprod, lprod


"""
    phi=[euler_phi(i) for i in bprod]
    for i in range(len(lprod)):
        diff=[lprod[i]-phi[i]]
    for i in range(len(lprod)):
        print bprod[i],lprod[i],phi[i],diff[i]
"""


def harmonic(n):
    """Harmonic - file:///home/tim/Sage/sage-6.3-i686-Linux/src/doc/output/html/en/thematic_tutorials/tutorial-programming-python.html"""
    harlist = [1 / i for i in srange(1, n + 1)]
    harsum = sum(harlist)
    return harsum.n()


def rbn(n):
    """Generate a random big integer of n digits"""
    biglist = []
    trailing = [1, 3, 7, 9]
    biglist.append(randint(1, 9))
    for i in range(n - 2):
        biglist.append(randint(0, 9))
    biglist.append(trailing[randint(0, 3)])
    bigint = int(''.join([str(i) for i in biglist]))
    return bigint


def rft(n, r):
    """
    rbn, factor, timeit
    Input: number of digits, number of repeats
    Return: list of tuples: (bn, time)
    no good: timeit returns an object of none type
    """


def rbns(n):
    """Generate a random big integer of n digits using string functions
    This actually fucking works. """
    bigstring = ''
    trailing = ['1', '3', '7', '9']
    bigstring += str(randint(1, 9))
    for i in range(n - 2):
        bigstring += str(randint(0, 9))
    bigstring += trailing[randint(0, 3)]
    bignum = int(bigstring)
    return bignum


def barp(l, n):
    """
    Bad Ass Random Prime
    outputs list of barps where:
        l = length of primes
        n = length of list
    Generate number (rbns), find next prime, divide by primes less than p, discard primes w/ low divisors.
    This is totally dipshit. The primes are PRIME!!
    """
    print 'generating raw prime list'
    raw_prime_list = [next_prime(rbns(l)) for i in range(n)]
    # barp_list = []
    # div_list = prime_range(3,1000000)
    """
    print 'generating barp list'
    for n in raw_prime_list:
        for m in div_list:
            if mod(n,m) == 0:
                break
            else:
                continue
        barp_list.append(n)
    return barp_list
    """
    return raw_prime_list


def makerandomlists(n):
    """Makes lists of four random ints from 1 to 100 """
    rl = []
    rs = []
    for i in range(n):
        rtup = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
        rl.append(rtup)
        rs.append(sum(rtup))
    return rl, rs


def shuffle():
    """ Shuffle a deck of cards"""
    udeck = range(52)
    sdeck = []
    while len(udeck) >= 1:
        card = udeck.pop(randint(0, len(udeck) - 1))
        sdeck.append(card)
    return (sdeck)


'''
north=[a[i] for i in range(len(a)) if i%4 == 0]
east=[a[i] for i in range(len(a)) if i%4 == 1]
south=[a[i] for i in range(len(a)) if i%4 == 2]
west=[a[i] for i in range(len(a)) if i%4 == 3]
'''


def bin(i):
    """ Make a binary string from an integer
    http://stackoverflow.com/questions/699866/python-int-to-binary """
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    return s


def make_list(random_num):
    ''' Makes lists of random numbers between 1 & 100, as long as the number 
    does not = 15. Takes the number of tries as input. Outputs 2-tuple: 
    length of lists, and list of lists.'''
    l = []
    while random_num != 15:
        l.append(random_num)
        random_num = random.randrange(1, 101)
    return l


def make_random_list():
    random_num = random.randrange(1, 101)
    new_list = make_list(random_num)
    return new_list


def main(n):
    list_of_lists = []
    list_of_counts = []
    counter = 0
    while counter < n:
        print 'counter =', counter
        new_list = make_random_list()
        list_of_lists.append(new_list)
        list_of_counts.append(len(new_list))
        counter += 1
    return (list_of_counts, list_of_lists)


def dice(n):
    """
    Throw a pair of dice n times. Returns  a dictionary of 
    value:frequency items.
    """
    import random

    l = []
    outcomelistkeys = range(2, 13)
    outcomelistvalues = [0 for i in range(12)]
    outcomedict = dict(zip(outcomelistkeys, outcomelistvalues))
    for i in range(n):
        d1 = random.randrange(6) + 1
        d2 = random.randrange(6) + 1
        l.append(d1 + d2)
    print "Mean = %.2f" % (stats.mean(l).n())
    print "Median = %.2f" % (stats.median(l).n())
    print "Std Dev = %.2f" % (stats.std(l).n())
    for i in l:
        outcomedict[i] += 1
    return outcomedict


def numbers(n):
    import time

    count = 0
    primelist = []
    for i in range(n):
        a = rbns(157)
        # print a
        if is_prime(a):
            print 'Bingo'
            count += 1
            primelist.append(a)
            # else: print 'Fuck you!'
            #time.sleep(.2)
    print count, 'Primes out of', n, 'total.'
    return primelist


def binth(p, q, m, n, terms=10):
    """
    Binomial Theorm see Journey Through Genius, p 167. 
    Requires arguments p,q,m,n. Optional terms.
    """
    m = float(m)
    n = float(n)
    binlist = []
    for i in range(terms):
        if i == 0:
            binlist.append(p ** (m / n))
        else:
            numerator = (m - n * (i - 1))
            denominator = n * i
            last = (numerator / denominator) * binlist[-1] * q
            binlist.append(last)
    return binlist


# ----------------------------------------------------------------------
def frange(arg0, arg1=None, arg2=None):
    """
    Summerfield p 71
    Returns a list of floats using range-like syntax
    frange(start, stop, inc)
    frange(start, stop)
    frange(stop)
    """
    start = 0.0
    inc = 1.0

    if arg2 is not None:  # 3 arguments given
        start = arg0
        stop = arg1
        inc = arg2
    elif arg1 is not None:  # 2 arguments given
        start = arg0
        stop = arg1
    else:  # 1 argument given
        stop = arg0
    # Build and return a list
    result = []
    while start < (stop - (inc / 2.0)):
        # yield start  # Uncomment if generator needed
        result.append(start)  # Comment if generator needed
        start += inc
    return result  # Comment if generator needed


# ----------------------------------------------------------------------
def tcsqrt(n, tries=8):
    """
    Take sqrt using algo found on p. 22-5 of Feynman
    """
    a = n / 2
    for i in range(tries):
        ap = (a + (n / a)) / 2
        a = ap
    return a.n()


def tcsqrtlist(n, t):
    try_list = []
    for i in range(1, t + 1):
        item = (i, tcsqrt(n, i))
        try_list.append(item)
    return try_list


# ----------------------------------------------------------------------
def payment(pv, term, i):
    """
    shit
    """
    interest = float(i) / 1200
    pymt = (pv * interest) / (1 - (1 + interest) ** (-term))
    print "Payment = %7.2f" % (pymt)
    return pymt


# ----------------------------------------------------------------------
def tosses(n):
    """
    Simulates number of heads in n coin tosses
    """
    outcome = []
    for i in range(n):
        outcome.append(randint(0, 1))
    return sum(outcome)


# ----------------------------------------------------------------------
def tossFreq(n, m):
    """
    Make a dictionary of outcome_number:frequency_of_outcomes
    input n, m where:
    n = number of tosses
    m = number of players tossing
    outcome number range = 0 to n+1
    """
    outcomelistkeys = range(n + 1)
    outcomelistvalues = [0 for i in range(n + 1)]
    outcomedict = dict(zip(outcomelistkeys, outcomelistvalues))
    for i in range(m):
        outcomedict[tosses(n)] += 1
    return outcomedict


# ----------------------------------------------------------------------
def poker():
    """
    http://www.sagemath.org/doc/reference/combinat/sage/combinat/tutorial.html
    
    """
    Suits = Set(["Hearts", "Diamonds", "Spades", "Clubs"])
    Values = Set([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])
    Cards = CartesianProduct(Values, Suits).map(tuple)
    Hands = Subsets(Cards, 5)
    return Hands.random_element()


def eatshit():
    pass


def plt(n):
    p = []
    for i in range(2, n + 1):
        if is_prime(i):
            p.append(i)
    return (p)


def primelist(n, l):
    """
    generate a list of n prime numbers of l digits.
    """
    pl = []
    for i in range(n):
        pl.append(next_prime(rbn(l)))
        print "Got ", i+1
    return pl


def grade():
    numgrade = input('Numeric grade: ')
    if numgrade >= 90:
        lettergrade = "A"
    elif numgrade >= 90:
        lettergrade = "A"
    elif numgrade >= 80:
        lettergrade = "B"
    elif numgrade >= 70:
        lettergrade = "C"
    elif numgrade >= 60:
        lettergrade = "D"
    else:
        lettergrade = "F"
    print 'Letter Grade =', lettergrade


class Person:
    def __init__(self, first, middle, last, age):
        self.first = first
        self.middle = middle
        self.last = last
        self.age = age


    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last + ' ' + str(self.age)


    def initials(self):
        return self.first[0] + self.middle[0] + self.last[0]


    def changeAge(self, amount):
        self.age += amount


class Shape:
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1


class Rectangle(Shape):
    def __init__(self, xcor, ycor, width, height):
        Shape.__init__(self, xcor, ycor)
        self.width = width
        self.height = height

    def __str__(self):
        retStr = Shape.__str__(self)
        retStr += ' width: ' + str(self.width) + ' height: ' + str(self.height)
        return retStr


