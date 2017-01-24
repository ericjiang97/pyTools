import json
import requests
import csv
import json
import os
import math
import numpy as np

def binarySearch(array,targetval, position, mode):
    minloc=0
    maxloc=len(array)-1
    while(minloc<=maxloc):
        middle=(maxloc+minloc)//2
        if(array[middle][position]==targetval):
            if(mode == "data"):
                return array[middle]
            elif(mode == "position"):
                return middle
            else:
                return -2
        elif(array[middle][position]>targetval):
            maxloc=middle-1
        elif(array[middle][position]<targetval):
            minloc=middle+1
    return -1

def oneDBinarySearch(array,targetval, mode):
    minloc=0
    maxloc=len(array)-1

    while(minloc<=maxloc):
        middle=(maxloc+minloc)//2
        if(array[middle]==targetval):
            if(mode == "data"):
                return array[middle]
            elif(mode == "position"):
                return middle
            else:
                return -2
        elif(array[middle]>targetval):
            maxloc=middle-1
        elif(array[middle]<targetval):
            minloc=middle+1
    return -1

# this module builds a faculty mapping to a user based on their userReviews
def facultyMapping(jsonArray):
    address = "https://api2.monplan.tech/units/"
    userReview = jsonArray['itemReviews']
    facultyData = []
    for i in userReview:
        unit = i["unitCode"]
        unitRating = i["rating"]
        targetURL = address + str(unit)
        r = requests.get(targetURL)
        output = r.json()
        faculty = output["Faculty"]
        pos = binarySearch(facultyData,faculty,"faculty", "position")
        if(pos == -1):
            data = {"faculty": faculty, "numberOfRating": 1, "rating": unitRating}
            facultyData.append(data)
        else:
            currentRating = facultyData[pos]["rating"]
            currentNumRating = facultyData[pos]["numberOfRating"]
            newNumRating = currentNumRating+1
            facultyData[pos]["numberOfRating"] = currentNumRating + 1
            facultyData[pos]["rating"] = ((currentRating+unitRating)/newNumRating)
    return facultyData


def compareFacultyMapping(target, comparisonTarget):
    diff = 0
    #Build List of Faculties
    facultyArray = []
    for i in range(0, len(target)):
        facultyArray.append(target[i]["faculty"])
    for j in range(0, len(comparisonTarget)):
        fac = comparisonTarget[j]["faculty"]
        check = oneDBinarySearch(facultyArray,fac, "")
        if(check == -1):
            facultyArray.append(fac)
    #Now Loop List of Faculties
    for i in facultyArray:
        itemI = binarySearch(target, i, "faculty", "data")
        itemJ = binarySearch(comparisonTarget, i, "faculty", "data")

        if(itemI == -1):
            scoreI = 0
        else:
            scoreI = itemI["rating"]
        if(itemJ == -1):
            scoreJ = 0
        else:
            scoreJ = itemJ["rating"]
        diff += abs((scoreI-scoreJ))
    distance = math.sqrt((diff/len(target)))
    return distance

def similarFaculties():
    pass

# main comparison engine
def main(userID):
    userSpace = open("data.json", "r")
    data = json.loads(userSpace.read())
    userSpace.close()

    userData = binarySearch(data, userID, "userID", "data")
    facultyMap = facultyMapping(userData) #mapping based of faculty's
    for i in data:
        if (i["userID"] != userID):
            otherUserID = i["userID"]
            otherUserData = binarySearch(data, otherUserID, "userID", "data")
            if(otherUserData != -1):

                otherUserFac = facultyMapping(otherUserData)

                facultyDistance = compareFacultyMapping(facultyMap, otherUserFac)
                print("Comparing")
                print(str(userID) + " and " + str(otherUserID))
                print(facultyDistance)
        else:
            pass

main(27849821)
