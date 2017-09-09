def shift(A, n):
    if n == 0:
        return A
    return [0] + shift(A, n-1)
    
def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0

    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))

    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))

def Mult(X, Y):

    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))

def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True

def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]

def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def add(A, B):
    # assume A and B are reversed bitstrings
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C

def Add(A,B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))

def exc_or(a, b, c):
    return (a ^ (b ^ c))

def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0 
        
def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def reverse(A):
    B = A[::-1]
    return B

def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0

def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))

def dec2bin(n):
    # creates binary number in reverse
    #print(n)
    if n == 0:
        return []

    # if negative store in 2's 
    #if n == -1:

    m = n // 2
    A = dec2bin(m)
    fbit = n % 2
    #print([fbit] + A)
    return [fbit] + A

def map(v):
    if v==[]:
        return '0'
    elif v ==[0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0,1]:
        return '2'
    elif v == [1,1]:
        return '3'
    elif v == [0,0,1]:
        return '4'
    elif v == [1,0,1]:
        return '5'
    elif v == [0,1,1]:
        return '6'
    elif v == [1,1,1]:
        return '7'
    elif v == [0,0,0,1]:
        return '8'
    elif v == [1,0,0,1]:
        return '9'   
        
def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0,1,0,1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))

def pad(X, Y):
    X1 = X[:]
    Y1 = Y[:]
    len_X1 = len(X1)
    len_Y1 = len(Y1)
    if len_X1 > len_Y1:
        for x in range(len_X1 - len_Y1):
            Y1.append(0)
    else:

        for x in range(len_Y1 - len_X1):
            X1.append(0)

    return (X1, Y1)


def flipBits(X):
    Y = []
    for j in range(len(X)):
        if X[j] == 0:
            Y.append(1)
        else:
            Y.append(0)
    return Y


def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)

    q = add(q, q)
    r = add(r, r)
    
    if not even(X):
        r = add(r,[1])

    if (not compare(r,Y) == 2):
        r = sub(r, Y)
        q = add(q, [1])

    return (q,r)

def Divide(X, Y):
    (q,r) = divide(dec2bin(X), dec2bin(Y))
    return (bin2dec(q), bin2dec(r))

def twosComplement(X):
    # X is a number that is already in twos complement (so positive numbers
    # should have an extra 0 at the beginning).
    # Returns the twos complement of X (as a binary number).
    X1 = flipBits(X)
    X1 = add(X1, [1])
    return X1

def twosComp2Dec(X):
    # Given a reversed bitstring that is stored in two's complement, the
    # function will return that number in decimal. The returned value
    # can be positive or negative depending on the last bit in the bitstring.
    if X[len(X) - 1] == 1:
        return bin2dec(twosComplement(X)) * -1

    return bin2dec(X)


def subtract(X, Y):
    #X and Y are positive numbers and are decimals
    #The returned value is a decimal number that can
    #be positive or negative.
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    
    return twosComp2Dec(sub(X1, Y1))
    


def sub(X, Y):
    # X and Y are positive, binary numbers
    # The result is the binary representation of X - Y in twos complement.
    (X1, Y1) = pad(X, Y)
    X1.append(0) #Add one extra bit for the flags for two's complement
    Y1.append(0)
    Y1 = twosComplement(Y1) #Subtract

    result = add(X1, Y1)

    # hack off extra carry bit
    if len(result) > len(X1):
        result = result[:len(result) - 1]
    
    return result
    
    

def exp(X, Y):
    # Takes in two reversed binary strings and returns
    # a binary string of X^Y.
    if zero(Y):
         return [1]
    z = exp(X, div2(Y))

    if even(Y):
        return mult(z, z)
    else:
        return mult(X, mult(z, z))

def gcd(X, Y):
    if zero(Y):
        return X
    (q, r) = divide(X, Y)
    return gcd(Y, r)

# h1
# problem 1.27
def proveInverseExists(n):
    N = bin2dec(n)
    # assume n is a bitstring
    #for i in range(N):
        #print(bin2dec(gcd(dec2bin(i), n)))
        #print(compare(gcd(dec2bin(i), n), [1]))
        #print()
    items = [i  for i in range(N + 1) if compare(gcd(dec2bin(i), n), [1]) == 0]
    print(items)
    print(len(items))
    #return len(items)

proveInverseExists(dec2bin(1331))
