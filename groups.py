import random


# Foregroup hex code to HTML string of group.
def hexToGroup(
    x: int, y: int, character: str, fgHex: str, bkgHex: str, zIndex: int, persistentData
):
    fgHex = fgHex.upper()
    match fgHex:
        case "#FFFFFF":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#000000":
            print("Error: This character should have been deleted and not passed here.")
            exit(-1)
        case "#111111":
            return fourByFourGlowGroup(
                x, y, character, fgHex, bkgHex, zIndex, persistentData
            )
        case "#000011":
            return consistentRandomTwinklingStar(
                x, y, character, fgHex, bkgHex, zIndex, persistentData
            )
        case "#110000":
            return theFogRises(x, y, character, fgHex, bkgHex, zIndex, persistentData)
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
        + str(x)
        + ";"
        + zIndexString(zIndex)
        + '"></div>'
    )


def consistentRandomTwinklingStar(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    starChars = ["+", "%", "*"]

    rand = random.Random()
    rand.seed(
        x * 1000 + y
    )  # Seed the randomness with the current position so it is consistend between runs

    # Random vars
    pulseDuration = round(rand.random() * 5 + 5, 2)
    pulseDelay = (
        round(rand.random() * pulseDuration, 2) * -1
    )  # make negative to aviod animation "startup lag"
    maxBrightness = round(min([rand.random() * 0.6 + 0.7, 1]), 2)
    minBrightness = round(max([maxBrightness - (rand.random() * 0.3 + 0.05), 0.2]), 2)
    twinkleDuration = pulseDuration
    twinkleDelay = round(pulseDelay - (0.25 * pulseDuration), 2)

    firstChar = starChars.pop(rand.randrange(len(starChars)))
    secondChar = "&#x2022;"  # starChars.pop(rand.randrange(len(starChars)))

    return (
        '<div class="twinkling-star pulsing-star" style="'
        + ("--twinkle-duration: " + str(twinkleDuration) + "s;")
        + ("--twinkle-delay: " + str(twinkleDelay) + "s;")
        + ("--pulse-duration: " + str(pulseDuration) + "s;")
        + ("--pulse-delay: " + str(pulseDelay) + "s;")
        + ("--max-brightness: " + str(maxBrightness) + ";")
        + ("--min-brightness: " + str(minBrightness) + ";")
        + (zIndexString(zIndex) + '">')
        + ("<span>" + firstChar + "</span>")
        + ("<span>" + secondChar + "</span>")
        + "</div>"
    )


def theFogRises(
    x: int, y: int, character: str, color: str, bkgHex: str, zIndex: int, persistentData
) -> str:
    return '<div class="the-fog-rises" style="z-index: zIndex;"><div><span style="color: rgb(207, 255, 112);top: calc(0 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(0 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(1 * var(--pixel-size));left: calc(0 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(1 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(2 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(1 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(1 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(1 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(1 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(0 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(1 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(2 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(2 * var(--pixel-size));left: calc(9 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(2 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(2 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(2 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(2 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(3 * var(--pixel-size));left: calc(0 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(1 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(2 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(3 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(3 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(4 * var(--pixel-size));left: calc(2 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(4 * var(--pixel-size));left: calc(9 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(4 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(4 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(9 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(5 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(6 * var(--pixel-size));left: calc(3 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(4 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(5 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(6 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(9 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(6 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(7 * var(--pixel-size));left: calc(7 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(7 * var(--pixel-size));left: calc(8 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(7 * var(--pixel-size));left: calc(9 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(7 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(8 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(8 * var(--pixel-size));left: calc(17 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(8 * var(--pixel-size));left: calc(18 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(8 * var(--pixel-size));left: calc(19 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(9 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(9 * var(--pixel-size));left: calc(12 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(9 * var(--pixel-size));left: calc(13 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(14 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(17 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(18 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(19 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(20 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(9 * var(--pixel-size));left: calc(21 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(10 * var(--pixel-size));left: calc(10 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(10 * var(--pixel-size));left: calc(11 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(15 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(17 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(18 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(19 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(20 * var(--pixel-size));">#</span><span style="color: rgb(143, 222, 93);top: calc(10 * var(--pixel-size));left: calc(21 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(11 * var(--pixel-size));left: calc(16 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(11 * var(--pixel-size));left: calc(17 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(11 * var(--pixel-size));left: calc(18 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(11 * var(--pixel-size));left: calc(19 * var(--pixel-size));">#</span><span style="color: rgb(207, 255, 112);top: calc(11 * var(--pixel-size));left: calc(20 * var(--pixel-size));">#</span></div></div>'.replace(
        "zIndex", str(zIndex)
    )
