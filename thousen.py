# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a for loop

def main():
    for i in range(1000, 2001):
        if i % 5 == 4:
            print(i)
        else:
            print(i, end=" ")


if __name__ == "__main__":
    main()
