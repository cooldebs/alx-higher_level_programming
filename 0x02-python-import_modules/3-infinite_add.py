#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = sys.argv

    sum = 0
    for i in range(1, len(count)):
        sum += int(count[i])
    print("{}".format(sum))
