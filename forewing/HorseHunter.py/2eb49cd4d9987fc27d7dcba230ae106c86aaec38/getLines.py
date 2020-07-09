VALID_LEVEL = ["max", "min", "mix"]
VALID_TARGET = ["female", "male", "mix"]

def getLines(config):

    linesFemale = []
    linesMale = []

    if config['level'] == "max" or config['level'] == "mix":
        with open("resources-max.txt", "r", encoding="utf-8") as resources:
            linesFemale += resources.readlines()

    if config['level'] == "min" or config['level'] == "mix":
        with open("resources-min.txt", "r", encoding="utf-8") as resources:
            linesFemale += resources.readlines()

    if config['target'] == "female":
        return linesFemale
    else:
        linesMale = [replaceF2M(s) for s in linesFemale]

        if config['target'] == "male":
            return linesMale
        else:
            return linesFemale + linesMale


replaceTable = [
    ['妈', '爸'],
    ['🐴', '👴'],
    ['🐎', '👴'],
    ["母亲",  "父亲"],
    ["母",  "公"],
    ["你吗",  "你爹"],
    ["逼",  "屌"],
    ["阴道",  "肛门"],
    ["处女",  "处男"],
    ["娘", "爹"],
    ["她",  "他"],
]


def replaceF2M(s):
    r = s
    for replace in replaceTable:
        r = r.replace(*replace)
    return r
