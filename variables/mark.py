PI = 3.14159265

# one = 1
# two = 2
# three = 3
one, two, three = 1,2,3
print(one)
print(two)
print(three)
#print("done.")
two = 4
print(two)
print(one)
Decimal = 1.1
print(Decimal)

stringVar = "SomeCharsForStringVar"
print(stringVar)
print(PI)

def aNewFunction():
    global two
    print(two)
    newVar = "World"
    print(newVar)
    return

aNewFunction()
#print(newVar)

Five = 3+2
print(Five)

count = 0
print("the value of count is:")
print(count)
count +=1
#count = count + 1
print(count)

#count = count * 3
#count = count / 3
count /=3
print(count)



