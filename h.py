t = int(input())


def convertFive(n):
    # Code here
    return int(str(n).replace('0','5'))

for i in range(t):
    print (convertFive(int(input().strip())))

