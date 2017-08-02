#Write a python function for the following declarations:
#Note: the location tuple contains: 
#(x-coordinate, y-coordinate, orientation)
#Note: orientation is N,S,E,W

import re

class Robot:
    def __init__(self, sLocation):
     #TODO: finish the constructor
     #Define locationX, locationY, orientation
     #using the given value
        self.coordinateX = sLocation[0]
        self.coordinateY = sLocation[1]
        self.orientation = sLocation[2]
        self.initial = (coordinateX,coordinateY,orientation)
        return self.initial
         

    def moveForward(self,sLocation,distance):
        #TODO: finish the moveForward definition
        #accepts the tuple of location and distance
        #returns a tuple of the new location
        #The coordinate modified (x or y) is dependent
        #upon the orientation
        return newLocation
    
    def rotate(self,sLocation, orientation):
        #TODO: finish the rotate definition
        #accepts the tuple of location and the 
        #new orientation
        #returns the tuple of the new loaction and
        #orientation
        return newLocation    
