import json
import math

chunksCount = 3
fileContents = ""
filePath = "example-project/ex-characterLayer-fog-2.json"
outFilePath = "example-project/ex-characterLayer-fog-2-chunked.html"
with open(filePath, "r") as file:
    fileContents = json.loads(file.read())

# Dimensions Format = `"dimensions": { "rows": 36, "cols": 64 }`
EXPECTED_DIMENSIONS = fileContents["dimensions"]

chunks = []
chunkWidth = math.ceil(EXPECTED_DIMENSIONS["cols"] / chunksCount)
for chunkNum in range(chunksCount):
    chunks.append("<div>")

unknownHexcodesSeen = []
persistentCharAttrData = []
grid = fileContents["grid"]
for rowNum in range(EXPECTED_DIMENSIONS["rows"]):
    for colNum in range(EXPECTED_DIMENSIONS["cols"]):
        # Special case: Skip cells with bkg color #FFFFFF.
        # Used to hide characters only needed to force ASCII Studio to export in the correct dimensions.
        if grid[rowNum][colNum]["bg"].upper() == "#FFFFFF":
            continue

        # Special case: Ignore whitespace
        if grid[rowNum][colNum]["char"] == " ":
            continue

        chunks[math.floor(colNum / chunkWidth)] += (
            '<span style="'
            + ("color: " + grid[rowNum][colNum]["fg"] + ";")
            + ("top: calc(" + str(rowNum) + " * var(--pixel-size));")
            + ("left: calc(" + str(colNum % chunkWidth) + " * var(--pixel-size));")
            + '">'
            + grid[rowNum][colNum]["char"]
            + "</span>"
        )

fileString = '<div class="the-fog-rises" style="z-index: zIndex;">'


for chunkNum in range(chunksCount):
    chunks[chunkNum] += "</div>"
    fileString += chunks[chunkNum]

fileString += "</div>"

with open(outFilePath, "w") as file:
    file.write(fileString)
