string = input()
CAM = "CAMBRIDGE"

for alpa in string:
    for cam in CAM:
        if alpa == cam:
            string = string.replace(alpa, "")
print(string)