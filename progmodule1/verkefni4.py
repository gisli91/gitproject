score = 0
par = 0
counter = 1

while counter < 19:
    par = int(input(f"Par of hole {counter}: "))
    score = int(input(f"Score on hole {counter}: "))
    if score >= (par +4):
        print("bad hole")
    if score == (par +3):
        print("triple bogey") 
    if score == (par + 2):
        print("double bogey")
    if score == (par + 1):
        print("bogey")
    if score == par:
        print("par")
    if score == (par - 1):
        print("birdie")
    if score == (par - 2):
        print("eagle")
    if score == (par - 3):
        print("albatross")
    if score < par - 3:
        print("invalid score")
    counter += 1
