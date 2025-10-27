DirectionalValues = {"E": 1, "N": 1, "S": -1, "W": -1}
DirectionalChanges = {
    "N": {
        "L": "W",
        "R": "E"
    },
    "S": {
        "L": "E",
        "R": "W"
    },
    "W": {
        "L": "S",
        "R": "N"
    },
    "E": {
        "L": "N",
        "R": "S"
    }
}

def solve(input_list):
    total_distance = 0
    CurrentDirection = "N"
    isThereNorth = False
    isThereEast = False
    
    for instruction in input_list:
        CurrentDirection = DirectionalChanges[CurrentDirection][instruction[0]]
        if CurrentDirection == "N":
            isThereNorth = True
        if CurrentDirection == "E":
            isThereEast = True
        if isThereEast and isThereNorth:
            break
        
    CurrentDirection = "N"
    
    for instruction in input_list:
        side = instruction[0]
        value = instruction[1::]
        CurrentDirection = DirectionalChanges[CurrentDirection][side]
        direction =  DirectionalValues[CurrentDirection]
        
        if not isThereNorth and CurrentDirection == "S":
            direction = 1
        
        if not isThereEast and CurrentDirection == "W":
            direction = 1
        
        total_distance += int(value) * direction
    
    return total_distance
