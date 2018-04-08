
def shield(strength: int, attack_pattern: str) -> bool:
    """
    Tests whether the shield can withstand the attack.

    >>> shield(2, "CS")
    True
    """
    charge = 1
    shot = 0
    for i in attack_pattern:
        if i == "C":
            charge = charge * 2
        else:
            shot += charge

    if shot > strength:
        return False

    return True


def split(attack_pattern: str) -> bool:
    """
    Checks if all the S's are at the beginning and all C's at the end.

    >>> split("SSSSCCCC")
    True
    """
    encounterC = False
    for k in attack_pattern:
        if k == "C":
            encounterC = True
        if encounterC and k == "S":
            return False
    return True


def test(strength: int, attack_pattern: str) -> int:
    """
    Checks whether a scenario can be hacked or not.
    """
    ap = attack_pattern
    count = 0
    primary_analysis = shield(strength, ap)

    if primary_analysis:
        return count
    if "C" not in ap and not primary_analysis:
        return -1

    while not split(ap):
        index = 0
        for k in range(len(ap) - 1):
            if ap[k] == "C" and ap[k+1] == "S":
                index = k
        if (index+1) == len(ap) - 1:
            new = ap[:index] + "S" + "C"
        else:
            new = ap[:index] + "S" + "C" + ap[index+2:]
        ap = new
        count += 1
        if shield(strength, ap):
            return count

    return -1

numdata = input()
listlines = []
for cas in range(int(numdata)):
    listlines.append(input())
case = 1
for k in listlines:
    num = ""
    index = 0
    while not k[index] == " ":
        num = num + k[index]
        index += 1
    attack = k[index + 1:]

    answer = test(int(num), attack)
    if answer == -1:
        show = "IMPOSSIBLE"
    else:
        show = str(answer)
    print("Case #" + str(case) + ": " + show)
    case += 1


# tryit = [[1,"CS"], [2, "CS"], [1, "SS"], [6, "SCCSSC"], [2, "CC"], [3, "CSCSS"]]
# for k in tryit:
#     print(test(k[0],k[1]))
#     print("\n")
