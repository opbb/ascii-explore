import random

# Foregroup hex code to HTML string of group.
def hexToGroup(x: int, y: int, character: str, fgHex: str, bkgHex: str, zIndex: int, persistentData):
    fgHex = fgHex.upper()
    match fgHex:
        case "#FFFFFF":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#000000":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#111111":
            return fourByFourGlowGroup(x, y, character, fgHex, bkgHex, zIndex, persistentData)
        case '#000011':
            return consistentRandomTwinklingStar(x, y, character, fgHex, bkgHex, zIndex, persistentData)
    return None


# Helper functions
def zIndexString(zIndex: int):
    return "z-index: " + str(zIndex) + ";"

def defaultStyleAttr(zIndex):
    return 'style="' + zIndexString(zIndex) + '"'

def bkgColorString(bkgHex: str):
    return "background-color: " + bkgHex + ";"


# === GROUPS ===


def fourByFourGlowGroup(
    x: int, y: int, character: str, fgHex: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    return (
        '<div class="absolute-overlay four-by-four-glow" style="--glow-delay: '
        + str(x) + ';'
        + zIndexString(zIndex)
        + '"></div>'
    )

def consistentRandomTwinklingStar(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    rand = random.Random()
    rand.seed(x * 1000 + y) # Seed the randomness with the current position so it is consistend between runs

    return ('<div class="twinkling-star" style="--twinkle-duration: ' + str(round(rand.random() * 4 + 3, 2)) + 's;--twinkle-delay: -' + str(round(rand.random() * 7, 2)) + 's;' + zIndexString(zIndex) + '"><span>*</span><span>+</span></div>')
