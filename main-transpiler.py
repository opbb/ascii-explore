import json
import os
import sys

import charTransFuncs

# Defaults
GROUPS_DIRECTORY = "groups/"
HEAD_FILE_PATH = "head.html"
SCRIPT_LINKS_FILE_PATH = "scriptLinks.html"
CURRENT_DIRECTORY_PATH = os.getcwd()
charArgIndex, groupArgIndex = -1, -1

HELP_TEXT = "Expected args: backgroundFile -c characterFile1 ... characterFileN -g groupFile1 ... groupFileM\nFile paths should be relative to the current directory."
for i in range(1, len(sys.argv)):
    match sys.argv[i]:
        case "-c":
            charArgIndex = i
        case "-g":
            groupArgIndex = i
        case "-h":
            print(HELP_TEXT)
            exit(0)
        case "--help":
            print(HELP_TEXT)
            exit(0)

if len(sys.argv) < 2:
    print("Error: Must include the background layer file as an argument.")
    exit(-1)

if charArgIndex == 1 or groupArgIndex == 1:
    print("Error: The first argument must be the background layer file.")
    exit(-1)


# Process command line arguments

bkgFilePath = sys.argv[1]

charFilePaths = None
if charArgIndex != -1:
    charFilePaths = sys.argv[
        (charArgIndex + 1) : (
            groupArgIndex if groupArgIndex > charArgIndex else len(sys.argv)
        )
    ]
    if len(charFilePaths) == 0:
        charFilePaths = None

groupFilePaths = None
if groupArgIndex != -1:
    groupFilePaths = sys.argv[
        (groupArgIndex + 1) : (
            charArgIndex if charArgIndex > groupArgIndex else len(sys.argv)
        )
    ]
    if len(groupFilePaths) == 0:
        groupFilePaths = None


# Check if given files exist

if not os.path.isfile(bkgFilePath):
    print('Error: Could not find given file "' + bkgFilePath + '"')
    exit(-1)

if charFilePaths != None:
    for charFilePath in charFilePaths:
        if not os.path.isfile(charFilePath):
            print('Error: Could not find given file "' + charFilePath + '"')
            exit(-1)

if groupFilePaths != None:
    for groupFilePath in groupFilePaths:
        if not os.path.isfile(groupFilePath):
            print('Error: Could not find given file "' + groupFilePath + '"')
            exit(-1)

if not os.path.isdir(GROUPS_DIRECTORY):
    print(
        'Error: Could not find the groups directory, which should be named  "'
        + GROUPS_DIRECTORY
        + '"'
    )
    exit(-1)

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

# List containing all layers in order
layers = []
currentLayerIndex = 0

# Make a generic table creation function?
# It seems like all the variety happens in the cells and in the outer table element
# Pass functions to define those two pieces.
# Could be fun?

# TODO: Process background
#       - ~~Define page dimensions~~
#       - ~~Create list of row strings~~
#       - Create cells, appending them to row string
#           - Give each cell a bkg color using the style property
#           - Throw out characters and foreground color
#           - Give each cell an ID according to this scheme: `id="COLUMN-ROW"`
#       - Append row strings together
#       - Add wrapping table HTML with `id="bkg-layer"`
fileContents = ""
with open(bkgFilePath, "r") as file:
    fileContents = json.loads(file.read())

EXPECTED_DIMENSIONS = fileContents["dimensions"]
rows = fileContents["grid"]
rowStrings = []
for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
    rowString = "<tr>"
    for colNum in range(EXPECTED_DIMENSIONS["cols"]):
        cellString = (
            '<td id="'
            + str(colNum)
            + "-"
            + str(rowNum)
            + '" style="background-color: '
            + rows[rowNum][colNum]["bg"]
            + '"></td>'
        )
        rowString += cellString

    rowString += "</tr>"
    rowStrings.append(rowString)

tableString = (
    '<table id="bkg-layer" style="z-index: 0;" cellspacing="0" cellpadding="0">'
)
for rowString in rowStrings:
    tableString += rowString
tableString += "</table>"

with open("testOut.html", "w") as file:
    file.write(tableString)

# TODO: Process character layers
#       - FOR EACH LAYER
#       - Create list of row strings
#       - Create cells, appending them to row string
#           - Special case: Check for #FFFFFF background color. Remove character if found.
#           - Add charTransFunc output to cell on background color
#       - Append row strings together
#       - Add wrapping table HTML with `class="character-layer" style="z-index: i;"`

# TODO: Process group layers
#       - FOR EACH LAYER
#       - FOR EACH CELL WITH BKG COLOR
#       - Generate group HTML with function
#       - Attach group to bkg cell, absolute pos (0,0), z-index of layer index

# TODO: Combine strings into one
#       - Combine all layer strings into one
#       - Append scripts links div string to the end
#       - Add head and body to template

# TODO: Export
#       - Export as one HTML File
