from asssignment_1 import * 

# Find_biggest among three
def test_Find_Biggest1():
    assert Find_Biggest(2,3,5) == 5


# 2_Armstrong Number
def test_armstrong_number1():
    assert armstrong_number(153) == "Armstrong number"
def test_armstrong_number2():
    assert armstrong_number(125) == "Not an Armstrong number"

# 3_Reverse number
def test_reverse_number():
    assert reverse_number(125) == 521


# 4_GCD
def test_gcd():
    assert Gcd(4,18) == 2
def test_gcd1():
    assert Gcd(4,18) != 1

# 5_Compute Gcd

# 6_Leapyear
def test_year():
    assert year(2020) == "leapyear"
def test_year1():
    assert year(2021) == "Not a leapyear"

# 7_Type of triangle - equilateral, isosceles, scalene, right angled
def test_triangle():
    assert triangle(12,12,12) == "Equilateral"
def test_triangle1():
    assert triangle(1,2,3) != "Rightangled"


# 9_Quadrant of a given point (x,y)
def test_Catesianplane():
    assert Catesianplane(1,1) == "lies in First quadrant"
def test_Catesianplane1():
    assert Catesianplane(-2,3) == "lies in Second quadrant"


# 10_Choice based arithmetic
def test_Arithmetic_z():
    assert Arithmetic(2,2,1) == 4
def test_Arithmetic_z1():
    assert Arithmetic(2,2,2) == 0


# 11_ Check if given character is vowel or consonant

def test_vowelConsonant():
    assert vowelConsonant('1') == "Consonant"
    assert vowelConsonant('a') == "Vowel"
    assert vowelConsonant('z') == "Consonant"
    assert vowelConsonant('i') != "Consonant"

#choice based arithmetic
def test_choice_user():
    assert choice_user(1,2,1) == 3
    assert choice_user(3,3,2) == 0
    assert choice_user(3,5,3) != 1
    assert choice_user(8,2,5) == "Wrong input..!!"
    assert choice_user(1,2,0) == "Wrong input..!!"

    
def factorial_of_number():
    assert factorial_of_number(5) == 120
    assert factorial_of_number(11) == 39916800
    assert factorial_of_number(7) == 5040
    assert factorial_of_number(0) == 1
    assert factorial_of_number(19) == 121645100408832000

def sum_of_factor():
    assert sum_of_factor(15) == 24
    assert sum_of_factor(11) == 12
    assert sum_of_factor(99) == 156
    assert sum_of_factor(0) == 1


def Digital_root():
    assert Digital_root(7895) == 2
    assert Digital_root(1999) == 1
    assert Digital_root(56547) == 9
    assert Digital_root(0) == 0
    assert Digital_root(7) == 7
    
def sum_of_triangular():
    assert sum_of_triangular(4) == 20
    assert sum_of_triangular(12) == 364
    assert sum_of_triangular(0) == 0
    assert sum_of_triangular(199) == 1333300