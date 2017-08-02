#Write a python function for the following declarations:

import re
import math

#all locations are tuples, which represent an x-y 
#coordinate pair.

#do not alter the printLocation function
def printLocation(location):
    print "Location = (%i, %i)" %(location[0],location[1])    
    
def moveForwardX(distance, startLocation):
    #TODO: Calculate the distance along the
    #X (horizontal) axis. 
    #Return the new location as a tuple of 
    #coordinates x and y
    newX = startLocation[0] + distance
    newY = startLocation[1]
    new = (newX,newY)
    return new

def moveForwardY(distance, startLocation):
    #TODO: Calculate the distance along the
    #Y (vertical) axis. 
    #Return the new location as a tuple of 
    #coordinates x and y
    newY = startLocation[1] + distance
    newX = startLocation[0]
    new = (newX,newY)
    return new

def calcDistance(distanceX, distanceY):
    #TODO: Return the straight line distance
    #From the start location to the end location
    #Recall: x*x*x = x**3 in python
    totalDistance = math.sqrt((distanceX**2 + distanceY**2))
    return totalDistance

def robotVelocity(distance, time):
    #TODO: Return velocity using the straight line
    #distance and the given time
    velocity = distance / time
    return velocity
    
