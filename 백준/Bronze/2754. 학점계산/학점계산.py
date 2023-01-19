c = input()
alpa = ["A", "B", "C", "D"]
plus = ["+", "0", "-"]
c_result = 0
if "A" in c:
    c_result = 4
elif "B" in c:
    c_result = 3
elif "C" in c:
    c_result = 2
elif "D" in c:
    c_result = 1
if "+" in c:
    c_result += 0.3
elif "-" in c:
    c_result -= 0.3
print(f"{c_result:.1f}")