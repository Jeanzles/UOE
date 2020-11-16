import math
dig1 = 0
dig2 = 0
dig3 = 0 
dig4 = 0
dig5 = 0
power = 0 
summ = 0 

for i in range(1,548835):
    if (i <= 9):
        print(i)
    elif (i >= 10 and i <=100):
        pass
    elif (i >= 100 and i < 1000):
        power = 3
        dig1 = i // 100 #gets the first digit
        mix3 = dig1*10 #if you // 10 it will give you the 1st and 2nd digits together... 
        dig2 = (i // 10) - mix3  #you only want the second one meaning i have to substract it from the second digit
        dig3 = i % 10 # gets last digit
        summ = (dig1**power + dig2**power + dig3**power)
        if summ == i:
            print(i)
        else:
            pass
    elif (i >= 1000 and i < 10000):
        power = 4
        dig1 = i // 1000             #gets the first digit
        mix4 = dig1*10              #you need to get the 1st digit * 10 to find second digit.
        dig2 = (i // 100) - mix4 #minus the answer by that to find second digit.
        mix42 = dig2*10            #when finding third digit you have to add the multiplication of first digit and...
        mix43 = dig1*100            #second digit and minus them together to find the third letter by itself
        summix4 = mix42+mix43  #adds them together
        dig3 = (i // 10)- summix4 #gets the third digit
        dig4 = i % 10 # last digit is pretty easy to get.s
        summ = (dig1**power + dig2**power + dig3**power + dig4**power)
        if summ == i:
            print(i)
        else:
            pass
    elif (i >=10000 and i < 100000):
        power = 5
        dig1 = i // 10000
        mix5 = dig1 * 10
        dig2 = (i // 1000) - mix5
        mix52 = dig1 * 100
        mix53 = dig2 * 10
        dig3 = (i // 100) - (mix52+mix53)
        mix54 = dig1 * 1000
        mix55 = dig2 * 100
        mix56 = dig3 * 10
        dig4 = (i // 10) - (mix54+mix55+mix56) #this uses the same logic as the others just multuplying divisors.
        dig5 = (i % 10)
        summ = (dig1**power + dig2**power + dig3**power + dig4**power + dig5**power) #finds the sum 
        if summ == i:
            print(i)
        else:
            pass
    elif (i >= 100000 and i < 600000):
        power = 6
        dig1 = i // 100000
        mix6 = dig1 * 10
        dig2 = (i // 10000) - mix6
        mix62 = dig1 * 100
        mix63 = dig2 * 10
        dig3 = (i // 1000) - (mix62+mix63)
        mix64 = dig1 * 1000
        mix65 = dig2 * 100
        mix66 = dig3 * 10
        dig4 = (i // 100) - (mix64+mix65+mix66)
        mix67 = dig1 * 10000
        mix68 = dig2 * 1000
        mix69 = dig3 * 100
        mix60 = dig4 * 10
        dig5 = (i // 10) - (mix67+mix68+mix69+mix60)
        dig6 = i % 10
        summ = (dig1**power + dig2**power + dig3**power + dig4**power + dig5**power+dig6**power) #finds the sum 
        if summ == i:
            print(i)
        else:
            pass
 
print("exercise 2")

for n in range(0,1001):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n, end=' ')
print()
print("exercise 3")

#GCD
def GCD(a, b):
    if (b > a):
        b, a = a, b
    while (b != 0):
        r = a % b
        a = b
        b = r
        print(a)
    return a
GCD(35,100)

print("exercise 4")

degree = int(input("give me a degree: "))
newdegree = (math.radians(degree))
print(newdegree)

def factorial(x):
    fact = 1
    for n in range(2, x + 1):
        fact = fact * n
    return(fact)
y=0
e_to_2 = 0
for i in range(0,16):
    e_to_2 = ((-1**i/factorial(i)))
    y = y + e_to_2
print(y)
