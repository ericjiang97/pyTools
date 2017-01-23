import math
import numpy as np

#person = [unitA, unitB, unitC, unitD]
unitsTable = ["ENG1001","FIT1045","FIT1047","FIT1049"]

ratingsMatrix = [[3, 2, 0, 0, 5],[4, 3, 5, 2],[2, 4, 1, 3],[1, 2, 3, 4],[5, 5, 5, 5],[0,0,0,0], [0, 0, 4.7, 3]]
a = np.array(ratingsMatrix)
stdDev = (np.std(a))
distance = 0 # set default distance to 0

def compare(target, comparisonTarget):
    diff = 0
    for i in target:
        for j in comparisonTarget:
            diff += abs(i-j)
    distance = math.sqrt((diff/len(target)))/stdDev
    return distance


def buildTree(targetUser, matrix):
    array = []
    for i in range(0, len(matrix)):
        if i!= targetUser:
            dist = compare(matrix[targetUser], matrix[i])
            pair = [i, dist]
            array.append(pair)
    return sorted(array, key=lambda array:array[1] )

def binarySearch(array,targetval, position):
    minloc=0
    maxloc=len(array)-1

    while(minloc<=maxloc):
        middle=(maxloc+minloc)//2
        if(array[middle][position]>targetval):
            maxloc=middle-1
        elif(array[middle][position]<targetval):
            minloc=middle+1
    return array[:middle]

def recommend(user, matrix, productTable, threshold):
    tree = buildTree(user, matrix)
    userRatings = matrix[user]
    missingUnits = []
    for i in range(0, len(userRatings)):
        if(userRatings[i] == 0):
            missingUnits.append([])
            missingUnits[-1].append(i)
            missingUnits[-1].append(productTable[i])
    #Build Similar User Information based off threshold
    similarUsers = (binarySearch(tree, threshold,1))

    for item in range(0, len(missingUnits)):
        currentMissing = missingUnits[item][0]
        currentMissingScore = 0
        for user in range(len(similarUsers)):
            currentUser = similarUsers[user][0]
            userScoreForUnit = matrix[currentUser][currentMissing]
            currentMissingScore += userScoreForUnit
        averageScore = currentMissingScore/len(similarUsers)
        missingUnits[item].append(averageScore)

    return sorted(missingUnits, key=lambda missingUnits:missingUnits[1] )


print(recommend(6, ratingsMatrix, unitsTable, 1.5))
