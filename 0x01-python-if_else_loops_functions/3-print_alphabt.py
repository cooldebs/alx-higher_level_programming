#!/usr/bin/python3
for alp in range(ord('a'), ord('z') + 1):
    if chr(alp) != 'e' and chr(alp) != 'q':
        print("{:c}".format(alp), end='')
