import sys
riverLocating = [int(input("Which number do you want the number to start at?\n"))]
river1 = [1]
river3 = [3]
river9 = [9]
for i in range(16384):
    number = riverLocating[i]
    number1 = river1[i]
    number2 = river3[i]
    number3 = river9[i]
    x = [int(a) for a in str(riverLocating[i])]
    y = [int(a) for a in str(river1[i])]
    z = [int(a) for a in str(river3[i])]
    w = [int(a) for a in str(river9[i])]
    for int1 in range(len(x)):
        number = number + int(x[int1])
    riverLocating.append(number)
    print(number)
    for int2 in range(len(y)):
        number1 = number1 + int(y[int2])
    river1.append(number1)
    for int3 in range(len(z)):
        number2 = number2 + int(z[int3])
    river3.append(number2)
    for int4 in range(len(w)):
        number3 = number3 + int(w[int4])
    river9.append(number3)

for i in range(16384):
    if riverLocating[i] in river1:
        print("River Starting with: " + str(riverLocating[0]) + " Meet River 1 at number " + str(riverLocating[i]))
        print(river1)
        sys.exit()

    if riverLocating[i] in river3:
        print("River Starting with: " + str(riverLocating[0]) + " Meet River 3 at number " + str(riverLocating[i]))
        print(river3)
        sys.exit()
    if riverLocating[i] in river9:
        print("River Starting with: " + str(riverLocating[0]) + " Meet River 9 at number " + str(riverLocating[i]))
        print(river9)
        sys.exit()
