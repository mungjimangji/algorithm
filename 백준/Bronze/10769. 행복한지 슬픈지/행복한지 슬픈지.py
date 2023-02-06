string = input()
emotion = ""
sad = 0
happy = 0

for i in string:
    emotion = emotion + i
    if ":-)" in emotion:
        happy += 1
        emotion = ""
    elif ":-(" in emotion:
        sad += 1
        emotion = ""
    emotion + i

if happy == 0 and sad == 0:
    print("none")
elif happy > sad:
    print("happy")
elif happy < sad:
    print("sad")
else:
    print("unsure")