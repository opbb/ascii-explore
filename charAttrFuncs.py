import random


def hexToCharAttributes(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
):
    bkgHex = bkgHex.upper()
    match bkgHex:
        case "#FFFFFF":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#222222":
            # This is the default bkg color, so just add the z-index.
            return defaultStyleAttr(color, zIndex)
        case "#0000AA":
            return makeFloaty(x, y, character, color, bkgHex, zIndex, persistentData)
        case "#0000BB":
            return makeGlow(x, y, character, color, bkgHex, zIndex, persistentData)
        case "#0000CC":
            return makeFountain(x, y, character, color, bkgHex, zIndex, persistentData)
        case "#0000DD":
            return makeFadeUnderwater(
                x, y, character, color, bkgHex, zIndex, persistentData
            )
        case "#0000EE":
            return makePulsingStar(
                x, y, character, color, bkgHex, zIndex, persistentData
            )
    return None


# Helper functions
def zIndexString(zIndex: int):
    return "z-index: " + str(zIndex) + ";"


def colorString(color: str):
    return "color: " + color + ";"


def defaultStyleAttr(color, zIndex):
    return 'style="' + zIndexString(zIndex) + colorString(color) + '"'


# Attr functions


def makeFloaty(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    return (
        'class="floaty-text" style="--i: '
        + str(x + y)
        + ";"
        + zIndexString(zIndex)
        + colorString(color)
        + '"'
    )


def makeGlow(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    return (
        'class="glow-pulse-text" style="--glow-delay: '
        + str(x)
        + ";"
        + zIndexString(zIndex)
        + colorString(color)
        + '"'
    )


def makeFountain(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    return defaultStyleAttr(color, zIndex)  # stub method


def makeFadeUnderwater(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    if "firstWaterYCoord" not in persistentData:
        persistentData["firstWaterYCoord"] = y
    return (
        'class="fade-underwater" style="--fade-depth: '
        + str(y - persistentData["firstWaterYCoord"] + 1)
        + ";"
        + zIndexString(zIndex)
        + colorString(color)
        + '"'
    )


def makePulsingStar(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    rand = random.Random()
    rand.seed(
        x * 1000 + y
    )  # Seed the randomness with the current position so it is consistend between runs

    # Random vars
    pulseDuration = round(rand.random() * 8 + 7, 2)
    pulseDelay = (
        round(rand.random() * pulseDuration, 2) * -1
    )  # make negative to aviod animation "startup lag"
    maxBrightness = round(min([rand.random() * 0.8 + 0.4, 1]), 2)
    minBrightness = round(max([maxBrightness - (rand.random() * 0.3 + 0.05), 0.2]), 2)

    return (
        'class="pulsing-star" style="'
        + ("--pulse-duration: " + str(pulseDuration) + "s;")
        + ("--pulse-delay: " + str(pulseDelay) + "s;")
        + ("--max-brightness: " + str(maxBrightness) + ";")
        + ("--min-brightness: " + str(minBrightness) + ";")
        + (zIndexString(zIndex) + '"')
    )
