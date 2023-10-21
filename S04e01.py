import re

regex = r"\b[A-Za-z0-9]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b"

if __name__ == "__main__":
    temp = input()

    if re.fullmatch(regex, temp) != None:
        print("OK")

    else:
        print("WRONG")
