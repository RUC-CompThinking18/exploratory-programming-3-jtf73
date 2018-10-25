import re
KingGeedorah = open("Important text.txt","r")
read = KingGeedorah.read()
def use_regex(l):
    if type(l) != str:
        raise TypeError("Do you think I'm a fool?")

    TakeMeToYourLeader = re.findall(r"\w*at\b",l)
    r = []
    for x in TakeMeToYourLeader:
        if len(x) > 3:
            r += x
    print r

use_regex(KingGeedorah)
