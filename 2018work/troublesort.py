
def troublesort(Q: list) -> list:
    done = False
    lyst = Q
    while not done:
        done = True
        for k in range(len(lyst) - 2):
            if lyst[k] > lyst[k + 2]:
                done = False
                lyst[k], lyst[k+2] = lyst[k+2], lyst[k]
    return lyst



def test(numelements: int, Q: list) -> int:
    check = troublesort(Q)
    if check == sorted(Q):
        return -1
    else:
        for k in range(numelements - 1):
            if check[k] > check[k + 1]:
                return k
    return 0



numdata = input()
listlines = []
for cas in range(int(numdata) * 2):
    listlines.append(input())
case = 1
length = 0
for k in range(len(listlines)):
    if k % 2 == 0:
        length = int(listlines[k])
    else:
        lst = []
        part = ""
        for w in listlines[k]:
            if not w == " ":
                part = part + w
            else:
                lst.append(int(part))
                part = ""
        lst.append(int(part))
        answer = test(length, lst)
        if answer == -1:
            show = "OK"
        else:
            show = str(answer)
        print("Case #" + str(case) + ": " + show)
        case += 1
