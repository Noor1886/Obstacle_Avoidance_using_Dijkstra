import pygame
from pygame import gfxdraw
import math

# function to check for obstacles
#checking the obsatcles with their line equations to determine if they lie inside or not

def obstacle_check(x: int, y: int):
    a1 = y + 0.58*x - 260.84
    a2 = x - 240
    a3 = y - 0.57*x + 60.84
    a4 = y + 0.57*x - 170.02
    a5 = x - 160
    a6 = y - 0.58*x - 29.98

    b = (x-300)**2 + (y-185)**2 -2025

    c1 = y + 1.23*x - 221.40
    c2 = y - 0.31*x - 178.85
    c3 = y- 0.85*x - 104.83
    c4 = y + 3.2*x - 452.77
    c5 = y + 0.15*x - 191.89

    x1 = x-5
    x2 = x-395
    y1 = y -5
    y2 = y - 245

    if((a1<=0 and a2<=0 and a3>=0 and a4>=0 and a5>=0 and a6<=0)) or b<=0 or (c2<=0 and c3>=0 and c5>=0) or (c1>=0 and c4<=0 and c5<=0) or (x1<=0 or x2>=0 or y1<=0 or y2>=0):
        return True
    else:
        return False




# Class to represent graph nodes

class graphNodes:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.cost = math.inf
        self.parent = None

# class to define point robot properties
class pointRobot:
    def __init__(self, initialLoc, goalLoc):
        self.initialLoc = initialLoc
        self.goalLoc = goalLoc

# To get low cost nodes
def popQ(priorityQueue):
    minCost = 0
    for item in range(len(priorityQueue)):
        if priorityQueue[item].cost < priorityQueue[minCost].cost:
            minCost = item
    return priorityQueue.pop(minCost)

def getNode(coordinates, priorityQueue):
    for items in priorityQueue:
        if items.coordinates == coordinates:
            return priorityQueue.index(items)
        else:
            return None

def moveUp(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1
    if yCoord > 0 and not(obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord, yCoord-1]
        return costToMove, newLoc
    else:
        return None, None

def moveDown(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1

    if yCoord < 250 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord, yCoord + 1]
        return costToMove, newLoc
    else:
        return None, None

def moveLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1

    if xCoord > 0 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord - 1, yCoord]
        return costToMove, newLoc
    else:
        return None, None

def moveRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1

    if xCoord > 0 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord + 1, yCoord]
        return costToMove, newLoc
    else:
        return None, None

def moveUpRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1.4

    if yCoord < 250 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord + 1, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def moveUpLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1.4

    if yCoord > 0 and xCoord > 0 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord - 1, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def moveDownLeft(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1.4

    if yCoord < 250 and xCoord > 0 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord - 1, yCoord + 1]
        return costToMove, newLoc
    else:
        return None, None

def moveDownRight(coordinates):
    xCoord = coordinates[0]
    yCoord = coordinates[1]
    costToMove = 1.4

    if yCoord < 250 and xCoord < 400 and not (obstacle_check(xCoord, yCoord)):
        newLoc = [xCoord, yCoord - 1]
        return costToMove, newLoc
    else:
        return None, None

def updateGameDisplay(gameDisplay, coordinates, yellow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.gfxdraw.pixel(gameDisplay, coordinates[0], coordinates[1], yellow)

    pygame.display.update()

def updateNodeLoc(action, coordinates):
    if action ==1:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUp(coordinates)
    if action == 2:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveRight(coordinates)
    if action == 3:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDown(coordinates)
    if action == 4:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveLeft(coordinates)
    if action == 5:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUpRight(coordinates)
    if action == 6:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDownRight(coordinates)
    if action == 7:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveDownLeft(coordinates)
    if action == 8:
        updateGameDisplay(gameDisplay, coordinates, yellow)
        return moveUpLeft(coordinates)

def findTotalNodes(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    count = 0
    if y > 0:
        count = count + 1
    if y < 200:
        count = count + 1
    if x > 0:
        count = count + 1
    if x < 300:
        count = count + 1
    if x < 300 and y > 0:
        count = count + 1
    if x > 0 and y > 0:
        count = count + 1
    if x < 300 and y < 200:
        count = count + 1
    if x > 0 and y < 200:
        count = count + 1
    return count

def solveDijkstra(pixelBot):
    startLoc = pixelBot.initialLoc
    goalLoc = pixelBot.goalLoc

    pygame.gfxdraw.pixel(gameDisplay, startNode[0], startNode[1], red)
    pygame.display.update()
    pygame.gfxdraw.pixel(gameDisplay, goalNode[0], goalNode[1], green)
    pygame.display.update()

    initialNode = graphNodes(startLoc)
    initialNode.cost = 0

    totalNodes = findTotalNodes(goalLoc)

    visitedNodes = []
    priorityQueue = [initialNode]
    actionList = [1, 2, 3, 4, 5, 6, 7, 8]
    visitedNodes_list = []
    iterations = 0

    while priorityQueue:
        currentLoc = popQ(priorityQueue)
        currentCoords = currentLoc.coordinates
        visitedNodes.append(str(currentCoords))
        visitedNodes_list.append(currentCoords)
        if iterations == totalNodes:
            return nextNode.parent

        for moves in actionList:
            actionCost, nextCoords = updateNodeLoc(moves, currentCoords)

            if nextCoords is not None:
                if nextCoords == goalLoc:
                    if iterations < totalNodes:
                        iterations = iterations + 1

                nextNode = graphNodes(nextCoords)
                nextNode.parent = currentLoc
                if str(nextCoords) not in visitedNodes:
                    nextNode.cost = actionCost + nextNode.parent.cost
                    visitedNodes.append(str(nextNode.coordinates))
                    visitedNodes_list.append((nextNode.coordinates))
                    # print("vis",nextNode.coordinates[0], nextNode.coordinates[1])
                    # for event in pygame.event.get():
                    #     if event.type == pygame.QUIT:
                    #         pygame.quit()
                    #         quit()
                    # for i in range(len(visitedNodes)):

                    pygame.gfxdraw.pixel(gameDisplay, nextNode.coordinates[0], nextNode.coordinates[1], (255, 255, 0))
                    pygame.display.update()
                    priorityQueue.append(nextNode)
                else:
                    existingNodeCoords = getNode(nextCoords, priorityQueue)
                    if existingNodeCoords is not None:
                        temporaryNode = priorityQueue[existingNodeCoords]
                        if temporaryNode.cost > actionCost + nextNode.parent.cost:
                            temporaryNode.cost = actionCost + nextNode.parent.cost
                            temporaryNode.parent = currentLoc
            else:
                continue
    return None

def backTrack(node):
    backTrackList = []
    backTrackList.append(node.parent)
    parent = node.parent
    if parent == None:
        return backTrackList
    while parent is not None:
        backTrackList.append(parent)
        parent = parent.parent
        if (parent == None):
            break
    finalTrackedPath = backTrackList.copy()
    return finalTrackedPath

print("Enter the initial position for the robot")
initialX = int(input("Enter the X point where the robot will start: "))
initialY = int(input("Enter the Y point where the robot will start: "))
goalX = int(input("Enter the X point where the robot should reach: "))
goalY = int(input("Enter the Y point where the robot should reach: "))

print("This is a point robot with the map with 5mm clearnace space")

# Pygame convention's origin lies at the top-left corner

initialY = 250 - initialY
goalY = 250 - goalY
size = 0
clearance = 0

# Checking if the user is within bounds

if initialX > 400 or initialY > 250 or initialX < 0 or initialY < 0 or obstacle_check(initialX, initialY):
    print("The start position of robot is out of the frame or is enclosed within the obstacle")
    exit(0)

if goalX > 400 or goalY > 250 or goalX < 0 or goalY < 0 or obstacle_check(goalX, goalY):
    print("The goal point is within the obstacle or out of map")
    exit(0)

startNode = [initialX, initialY]
goalNode = [goalX, goalY]

pixelBot = pointRobot(startNode, goalNode)

# Building the obstacle space in pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (0, 255, 255)

gameDisplay = pygame.display.set_mode((400, 250))
gameDisplay.fill(black)
# Drawing circle
pygame.draw.circle(gameDisplay, red, (300, 185), 45)
# Drawing hexagon
pygame.draw.polygon(gameDisplay, red, ((200, 54.5), (240, 79.75), (240, 120.25), (200, 145.5), (160, 120.25), (160, 79.75)))
# Drawing convex polygon
pygame.draw.polygon(gameDisplay, red, ((105, 95), (85, 180), (115, 215), (31, 185)))



finalOutput = solveDijkstra(pixelBot)
print("Mission Accomplished")
if finalOutput is not None:
    tracedPath = backTrack(finalOutput)
    print("Back Track")
    for items in tracedPath:
        xCoord = items.coordinates[0]
        yCoord = items.coordinates[1]
        gfxdraw.pixel(gameDisplay, xCoord, yCoord, blue)
        pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pass

