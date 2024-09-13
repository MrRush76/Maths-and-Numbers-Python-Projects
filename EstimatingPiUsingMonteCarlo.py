import random
INTERVAL = int(input("How many points would you like to generate (the more points the more accurate the estimation of pi will be)\n"))
squarePoints = 0 # initiaizes squarePoints and circlePoints to count how many pooints have been generated throught the program
circlePoints = 0
for i in range(INTERVAL): # starts a loop for how many points need ot be generated

    x_point = random.uniform(-1, 1) # generates a random decimal number between -1 and 1 
    y_point = random.uniform(-1, 1)

    d = x_point**2 + y_point**2  # adds the square of each point 
    if d <= 1: #checks if the result is less than or equal to 1 to mimic checking if the point is inside of the radius of the circle due to xsquared + ysquared being equal to the radius sqaured which is one in our case 
        circlePoints = circlePoints + 1 # increases the amount of points generated inside the circle 
    squarePoints = squarePoints + 1 # all points will generate within the square if they are between -1 and 1 as it had to be increased no matter what
pi = 4 * (circlePoints / squarePoints) #re arranging the ratio of points inside an out gives us a formula to calculate pi by using the formula for radius and the amount of points inside the circle and square we have generated 
print("An estimation of pi using: " + str(INTERVAL) + " points is " + str(pi)) # prints an estimation of pi depending on how many points (the more points there are the more accurate the estimation will be up to a certain degree of accuracy)
