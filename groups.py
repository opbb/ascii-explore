# Foregroup hex code to HTML string of group.
def hexToGroup(x: int, y: int, character: str, fgHex: str, bkgHex: str, zIndex: int):
    fgHex = fgHex.upper()
    match fgHex:
        case "#FFFFFF":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#000000":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#111111":
            return fourByFourGlowGroup(x, y, character, fgHex, bkgHex, zIndex)
    return None


# Helper functions
def zIndexString(zIndex: int):
    return "z-index: " + str(zIndex) + ";"


def bkgColorString(bkgHex: str):
    return "background-color: " + bkgHex + ";"


def fourByFourGlowGroup(
    x: int, y: int, character: str, fgHex: str, bkgHex: str, zIndex: int
) -> str:
    return (
        '<div class="absolute-overlay four-by-four-glow" style="'
        + zIndexString(zIndex)
        + '"></div>'
    )
