import sys

output = True
allUsers = []

try:
    sys.argv[1]
except Exception:
    print("Syntax: python3 script.py users.txt")
    print("Syntax with output: python3 script.py users.txt output.txt")
    sys.exit("Error: no arguments provided!")
try:
    sys.argv[2]
    sys.argv[3]
except Exception:
    output = False
    pass
try:
    f = open(sys.argv[1], "r")
except Exception:
    print("Unable to find file: '" + str(sys.argv[1]) + "'! (check read permissions/spelling)")
    sys.exit(1)

for line in f.readlines():
    if "VALID USERNAME:" in line:
        value = line[(line.find("VALID USERNAME:") + len("VALID USERNAME:")):(line.find("@"))].replace(" ", "").lower()
        if value.lower() not in allUsers:
            allUsers.append(value.lower())

f.close()

for user in allUsers:
    print(user)

try:
    f = open(sys.argv[2], "w")
    for user in allUsers:
        f.writelines(user + "\n")
    f.close()
except Exception:
    print("Error: " + str(Exception) + "!")
