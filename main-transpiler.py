import json
import os
import sys

import charAttrFuncs
import groups

# Defaults
GROUPS_DIRECTORY = "groups/"  # Unused currently. Id like to give each group it's own file, but havent set that up yet
HEAD_FILE_PATH = "head.html"
SCRIPT_LINKS_FILE_PATH = "scriptLinks.html"
CURRENT_DIRECTORY_PATH = os.getcwd()
charArgIndex, groupArgIndex = -1, -1
persistentCharAttrData = {}
persistentGroupsData = {}

HELP_TEXT = "Expected args: backgroundFile [-c characterFile]* [-g groupFile]*\nEach character/group file must be preceeded by its option.\nFiles should be listed in order of z-index.\nFile paths should be relative to the current directory."

if len(sys.argv) < 2:
    print("Error: Must include the background layer file as an argument.")
    exit(-1)

layerCounter = 1
layerFilePaths = [sys.argv[1]]
charLayerIndices = []
groupLayerIndices = []
for i in range(1, len(sys.argv)):
    match sys.argv[i]:
        case "-h":
            print(HELP_TEXT)
            exit(0)
        case "--help":
            print(HELP_TEXT)
            exit(0)

    if i == 1:
        if sys.argv[i] == "-c" or sys.argv[i] == "-g":
            print("Error: First argument must be the background file.")
            exit(-1)
        continue

    match sys.argv[i]:
        case "-c":
            if len(sys.argv) <= (i + 1):
                print('Error: Trailing "-c" is missing its file path.')
                exit(-1)
            layerFilePaths.insert(layerCounter, sys.argv[i + 1])
            charLayerIndices.append(layerCounter)
            layerCounter += 1

        case "-g":
            if len(sys.argv) <= (i + 1):
                print('Error: Trailing "-g" is missing its file path.')
                exit(-1)
            layerFilePaths.insert(layerCounter, sys.argv[i + 1])
            groupLayerIndices.append(layerCounter)
            layerCounter += 1


# Process command line arguments

# Check if given files exist

if not os.path.isfile(layerFilePaths[0]):
    print('Error: Could not find given background file "' + layerFilePaths[0] + '"')
    exit(-1)

for layerIndex in charLayerIndices:
    if not os.path.isfile(layerFilePaths[layerIndex]):
        print(
            'Error: Could not find given character file "'
            + layerFilePaths[layerIndex]
            + '"'
        )
        exit(-1)

for layerIndex in groupLayerIndices:
    if not os.path.isfile(layerFilePaths[layerIndex]):
        print(
            'Error: Could not find given group file "'
            + layerFilePaths[layerIndex]
            + '"'
        )
        exit(-1)

# if not os.path.isdir(GROUPS_DIRECTORY):
#     print(
#         'Error: Could not find the groups directory, which should be named  "'
#         + GROUPS_DIRECTORY
#         + '"'
#     )
#     exit(-1)

if not os.path.isfile(HEAD_FILE_PATH):
    print(
        'Error: Could not find the HTML head file, which should be named  "'
        + HEAD_FILE_PATH
        + '"'
    )
    exit(-1)

if not os.path.isfile(SCRIPT_LINKS_FILE_PATH):
    print(
        'Error: Could not find the scripts file, which should be named  "'
        + SCRIPT_LINKS_FILE_PATH
        + '"'
    )
    exit(-1)

currentLayerIndex = 0

# Make a generic table creation function?
# It seems like all the variety happens in the cells and in the outer table element
# Pass functions to define those two pieces.
# Could be fun?

fileContents = ""
with open(layerFilePaths[0], "r") as file:
    fileContents = json.loads(file.read())

# Dimensions Format = `"dimensions": { "rows": 36, "cols": 64 }`
EXPECTED_DIMENSIONS = fileContents["dimensions"]

# 3d list of HTML strings, containing the contents of the canvas to be inserted into the containing bkg grid
canvasGrid = []
for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
    canvasGrid.insert(rowNum, [])
    for colNum in range(EXPECTED_DIMENSIONS["cols"]):
        canvasGrid[rowNum].insert(colNum, [])

# Process character layers
unknownHexcodesSeen = []
for layerIndex in charLayerIndices:
    with open(layerFilePaths[layerIndex], "r") as file:
        fileContents = json.loads(file.read())

    if fileContents["dimensions"] != EXPECTED_DIMENSIONS:
        print(
            'Error: Character layer "'
            + layerFilePaths[layerIndex]
            + '" does not match expected dimensions.'
        )
        exit(-1)

    grid = fileContents["grid"]
    for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
        for colNum in range(EXPECTED_DIMENSIONS["cols"]):
            # Special case: Skip cells with bkg color #FFFFFF.
            # Used to hide characters only needed to force ASCII Studio to export in the correct dimensions.
            if grid[rowNum][colNum]["bg"] == "#ffffff":
                continue

            # Special case: Ignore whitespace
            if grid[rowNum][colNum]["char"] == " ":
                continue

            # Get character attributes
            charAttributes = charAttrFuncs.hexToCharAttributes(
                colNum,
                rowNum,
                grid[rowNum][colNum]["char"],
                grid[rowNum][colNum]["fg"],
                grid[rowNum][colNum]["bg"],
                layerIndex,
                persistentCharAttrData,
            )

            if charAttributes is None:
                charAttributes = 'style="z-index: ' + str(layerIndex) + ';"'

                if grid[rowNum][colNum]["bg"] not in unknownHexcodesSeen:
                    print(
                        'Error: Could not find character transformation function corresponding to the hex code "'
                        + grid[rowNum][colNum]["bg"]
                        + '"'
                    )
                    unknownHexcodesSeen.append(grid[rowNum][colNum]["bg"])

            canvasGrid[rowNum][colNum].append(
                "<span "
                + charAttributes
                + ">"
                + grid[rowNum][colNum]["char"]
                + "</span>"
            )


# TODO: Process group layers
#       - FOR EACH LAYER
#       - FOR EACH CELL WITH FG COLOR
#       - Generate group HTML with function
#       - Attach group to bkg cell, absolute pos (0,0), z-index of layer index

unknownGroupCodesSeen = []
for layerIndex in groupLayerIndices:
    with open(layerFilePaths[layerIndex], "r") as file:
        fileContents = json.loads(file.read())

    if fileContents["dimensions"] != EXPECTED_DIMENSIONS:
        print(
            'Error: Group layer "'
            + layerFilePaths[layerIndex]
            + '" does not match expected dimensions.'
        )
        exit(-1)

    grid = fileContents["grid"]
    for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
        for colNum in range(EXPECTED_DIMENSIONS["cols"]):
            if (
                grid[rowNum][colNum]["fg"].upper() == "#FFFFFF"
                or grid[rowNum][colNum]["fg"] == "#000000"
                or grid[rowNum][colNum]["fg"] == "rgb(255, 255, 255)"
                or grid[rowNum][colNum]["fg"] == "rgb(0, 0, 0)"
            ):
                # White or black are default, ignore them.
                continue
            groupString = groups.hexToGroup(
                colNum,
                rowNum,
                grid[rowNum][colNum]["char"],
                grid[rowNum][colNum]["fg"],
                grid[rowNum][colNum]["bg"],
                layerIndex,
                persistentGroupsData,
            )

            if groupString is None:
                if grid[rowNum][colNum]["fg"] not in unknownGroupCodesSeen:
                    print(
                        'Error: Could not find group corresponding to the hex code "'
                        + grid[rowNum][colNum]["fg"]
                        + '"'
                    )
                    unknownGroupCodesSeen.append(grid[rowNum][colNum]["fg"])
                continue

            canvasGrid[rowNum][colNum].append(groupString)


# TODO: Process background
#       - ~~Define page dimensions~~
#       - ~~Create list of row strings~~
#       - Create cells, appending them to row string
#           - Give each cell a bkg color using the style property
#           - Throw out characters and foreground color
#           - Give each cell an ID according to this scheme: `id="COLUMN-ROW"`
#       - Append row strings together
#       - Add wrapping table HTML with `id="bkg-layer"`
with open(layerFilePaths[0], "r") as file:
    fileContents = json.loads(file.read())

grid = fileContents["grid"]
rowStrings = []
for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
    rowString = "<div>"
    for colNum in range(EXPECTED_DIMENSIONS["cols"]):
        cellString = (
            '<span id="'
            + str(colNum)
            + "-"
            + str(rowNum)
            + '" style="background-color: '
            + grid[rowNum][colNum]["bg"]
            + '">'
            + "".join(canvasGrid[rowNum][colNum])
            + "</span>"
        )
        rowString += cellString

    rowString += "</div>"
    rowStrings.append(rowString)

gridString = '<div id="bkg-layer" class="layer" style="z-index: 0;">'
for rowString in rowStrings:
    gridString += rowString
gridString += "</div>"

# TODO: Combine strings into one
#       - Combine all layer strings into one
#       - Append scripts links div string to the end
#       - Add head and body to template
fileString = '<!doctype html><html lang="en">'

# HTML Head
with open(HEAD_FILE_PATH, "r") as file:
    fileContents = file.read()
fileString += fileContents

# HTML Body
fileString += '<body><div id="world-container">'
fileString += gridString
fileString += "</div>"  # close world container
# Post-Body Scripts
with open(SCRIPT_LINKS_FILE_PATH, "r") as file:
    fileContents = file.read()
fileString += fileContents

fileString += "</body>"

# TODO: Export
#       - Export as one HTML File
with open("testOut.html", "w") as file:
    file.write(fileString)
