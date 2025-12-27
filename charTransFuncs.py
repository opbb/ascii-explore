def hexToFunction(hex: str):
    match hex:
        case "#FFFFFF":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#222222":
            # This is the default bkg color, do nothing.
            return ""
        case "#0000AA":
            return makeFloaty
        case "#0000BB":
            return makeGlow
        case "#0000CC":
            return makeFountain
        case "#0000DD":
            return makeFadeUnderwater

    # We should have returned by now
    print(
        'Error: Could not find character transformation function corresponding to the hex code "'
        + hex
        + '"'
    )
    return None


def makeFloaty(x: int, y: int, character: str, color: str, bkgColor: str) -> str:
    return 'class="floaty-text" style="--i: ' + str(x + y) + ';"'


def makeGlow(x: int, y: int, character: str, color: str, bkgColor: str) -> str:
    return ""  # stub method


def makeFountain(x: int, y: int, character: str, color: str, bkgColor: str) -> str:
    return ""  # stub method


def makeFadeUnderwater(
    x: int, y: int, character: str, color: str, bkgColor: str
) -> str:
    return ""  # stub method
