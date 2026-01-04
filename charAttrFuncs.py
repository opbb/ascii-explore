def hexToCharAttributes(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int
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
            return makeFloaty(x, y, character, color, bkgHex, zIndex)
        case "#0000BB":
            return makeGlow(x, y, character, color, bkgHex, zIndex)
        case "#0000CC":
            return makeFountain(x, y, character, color, bkgHex, zIndex)
        case "#0000DD":
            return makeFadeUnderwater(x, y, character, color, bkgHex, zIndex)
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
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int
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
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int
) -> str:
    return defaultStyleAttr(color, zIndex)  # stub method


def makeFountain(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int
) -> str:
    return defaultStyleAttr(color, zIndex)  # stub method


def makeFadeUnderwater(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int
) -> str:
    return defaultStyleAttr(color, zIndex)  # stub method
