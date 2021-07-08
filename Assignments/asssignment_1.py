import math

# 1_Biggest of three/four numbers
def Find_Biggest(a,b,c):
    if (a >= b) and (a >= b):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

# 2_Check if given number is armstrong or not
def armstrong_number(x):
    temp = x
    tempr_v = 0
    count = 0
    temp1 = x
    while temp1 > 0:
        count = count + 1
        temp1 = temp1//10
    while temp > 0:
        rem = temp % 10 
        tempr_v = (rem ** count) + tempr_v  
        temp = temp // 10  
    if x == tempr_v:
        return "Armstrong number"    
    else:
        return "Not an Armstrong number"
       
# 3_ Reverse the number, sum of digits
def reverse_number(x):
    rev_num = 0
    while x > 0:
        last_digit = x % 10
        rev_num = rev_num*10 + last_digit
        x = x // 10
    return rev_num
# 4_GCD/HCF of two numbers
def Gcd(x, y):
    return math.gcd(x,y)

# 5_LCM without computing GCD/HCF

def compute_Gcd(x, y):
    if x>y:
        greatest=x
    else:
        greatest=y
    while(1):
        if greatest%x==0 and greatest%y==0:
            lcm= greatest
            break
        greatest += 1
    return lcm

# 6_Check if given year is Leap year or not
def year(x):
    if((x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))):
        return "leapyear"
    else:
        return "Not a leapyear"
# 7_Type of triangle - equilateral, isosceles, scalene, right angled
def triangle(x,y,z):
    if(x == y == z):
        return "Equilateral"
    if(x == z or y == z or z == x):
        return "Isosceles"
    if(z**2 == x**2 + y**2 or y**2 == z**2 + x**2 or x**2 == y**2 + z**2):
        return "Rightangled"
    else:
        return "Scalene"


# 8_Roots of a quadratic equation
def RofQE(x,y,z):
    d = (y**y)-(4*x*z)
    if d>0:
        root1 = (-y-math.sqrt(d))/(2*x)
        root2 = (-y+math.sqrt(d))/(2*x)
        return root1,root2
    elif d==0:
        root=(-y+math.sqrt(d))/(2*x)
        return root
    else:
        real=(-y/(2*x))
        complex= math.sqrt(abs(d))/(2*x)
        return real,complex


# 9_Quadrant of a given point (x,y)

def Catesianplane(x,y):
    if (x > 0 and y > 0):
        return "lies in First quadrant"
    elif (x < 0 and y > 0):
        return "lies in Second quadrant"     
    elif (x < 0 and y < 0):
        return"lies in Third quadrant" 
    elif (x > 0 and y < 0):
        return "lies in Fourth quadrant"
    elif (x == 0 and y == 0):
        return "lies at origin"

# 10_Choice based arithmetic
def Arithmetic(x,y,z):
    if ( z == 1 ):
        return x + y
    elif ( z == 2 ):
        return x - y
    elif ( z == 3):
        return x * y
    elif ( z == 4):
        return x / y

# 11-Check if given character is vowel or consonant
def vowelConsonant(x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        return("Vowel")
    else:
        return("Consonant")


#12-choice based arithmetic

def choice_user(num1,num2,choice):
    if (choice >= 1 and choice <= 4):
        if choice == 1:  # To add two numbers
            tempr_v = num1 + num2
            return (tempr_v)
        elif choice == 2:  # To subtract two numbers
            tempr_v = num1 - num2
            return (tempr_v)
        elif choice == 3:  # To multiply two numbers
            tempr_v = num1 * num2
            return (tempr_v)
        elif choice == 4:  # To get quotient with decimal value
            tempr_v = num1 / num2
            return (tempr_v)
        elif choice == 5:
            exit()
        else:
            return ("Wrong input..!!")
    else:
        return ("Wrong input..!!")
        

# 13-_Fibonacci sequence, Tribonacci series
def Fibonacci_series(x):
    n1=0                                         
    n2=1                                         
    if x<=0:
        return 0
    if x==1:
        return 1
    else:
        for x in range(2,x):
            next=n1+n2                           
            n1=n2
            n2=next
            print (next)

# 13* Factorial of a given number
def factorial_of_number(x):
    fact=1
    for i in range(1, x+1):
        fact=fact*i
    print(fact)

# 14_Sum of the factors, n=30, 1+2+3+5+6+10+15
def sum_of_factor(x):
  factor = [1]
  for i in range(2,x+1):
     if x%i==0:
         factor.append(i)
  return(sum(factor))


# 15_Digital root of a given number, 7895 -> 29 -> 11 -> 2
def Digital_root(x):
    if x>0 and x<10:
        return(x)
    else:
        sum=0
        temp=1
        while temp:
            sum=0
            while x>0:
                digit=x%10
                x=x//10
                sum=sum+digit
            if sum<10:
                temp=0
            else:
                x=sum
        return(sum)


# 16_List/count of prime numbers for given range
def prime_range(x):
    for j in range(1,x):
        for i in range(2,j):
            if (j%i==0):
                break
            else:
                return j


# 16_List/count of prime numbers for given range
def prime_numbers_for(x):
    for j in range(1,x):
        for i in range(2,j):
            if (j%i==0):
                break
            else:
                return(j)


# 17_Sum of triangular numbers, n=4, 1 + (1+2) + (1+2+3) + (1+2+3+4) = 20
def sum_of_triangular(x):
    sum = 0
    while x > 0:
        for i in range(1,x+1):
            sum +=i
        x -=1
    return sum


# 18_Maximum number by deleting single digit in a 4 digit number 5872  - 872,   9865 - 985
def maximum_num_deleting(x, y):
    for i in range(0, y):
        result = 0
        i = 1
        while x // i > 0:
            temp = (x // (i * 10)) * i + (x % i)
            i *= 10
            if temp > result:
                result = temp
        x = result
    return(result)


# 19_Generate super prime numbers
def Super_Prime_inner(x, Prime):
    Prime[0] = Prime[1] = False
    for i in range(2,x+1):
        Prime[i] = True
    for p in range(2,x+1):
        if (p*p<=x and Prime[p] == True):
            for i in range(p*2,x+1,p):
                Prime[i] = False
                p += 1
def Super_Primes_main(x):
    Prime = [1 for i in range(x+1)]
    Super_Prime_inner(x, Prime)
    primes = [0 for i in range(2,x+1)]
    j = 0
    for p in range(2,x+1):
       if (Prime[p]):
           primes[j] = p
           j += 1
    for k in range(j):
        if (Prime[k+1]):
            print (primes[k])


# 20_No.of combinations for n teams to play each other,  i.e. nCr
def nCr(n,r):
    print((fact1(n)/(fact1(r)*fact1(n-r))))
def fact1(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    print(result)


# 21_Generate number triangles/pyramids, pascal triangle
def generation(x):
    for i in range(1, x + 1):
        for j in range(0, x - i + 1):
            print(' ', end='')
        y = 1
        for j in range(1, i + 1):
            print(' ', y, sep='', end='')
            y = y * (i - j) // j
        print()


# Number triangle
def onr_sided_triangel(x):
    n = 1
    for i in range(0, x):
        n = 1
        for j in range(0, i+1):
            print(n, end=" ")
            n = n + 1
        print("\r")
