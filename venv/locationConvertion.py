# NTB = 1366x768
##PC = 1920x1080

oldResolution = [1920, 1080]
newResolution = [1366, 768]

view1Location = [785, 496]


def newCoordsFnc(oldCoords):
    newCoords = []
    newCoordsX = oldCoords[0] / oldResolution[0] * newResolution[0]
    newCoords.append(newCoordsX)
    newCoordsY = oldCoords[1] / oldResolution[1] * newResolution[1]
    newCoords.append(newCoordsY)
    print(newCoords)
    return newCoords


newCoordsFnc(view1Location)
